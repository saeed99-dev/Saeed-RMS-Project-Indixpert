from datetime import datetime
from src.model.models import PathModel
from src.filehandling.filemode import Filemode
from src.utils.tools import staff_subheading
from src.domain.usersdata import User
from src.domain.table_menu import TableManager
from src.security.validation import Validator
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


class Menu:
    def __init__(self):
        try:
            self.cart = []
            self.menu = Filemode().load_data(PathModel().menu_data)
            self.order_history = Filemode().load_data(PathModel().order_data)
        except Exception as e:
            print(f"{Fore.RED}Initialization Error: {e}")

    def dislay_menu(self):
        try:
            staff_subheading("RESTAURANT MENU")

            for category, items in self.menu.items():
                print(f"\n{Fore.MAGENTA}{category.upper()}")
                print(Fore.BLUE + "-" * 60)
                print(
                    f"{Fore.BLUE}| {Fore.YELLOW}{"Name":<25}{Fore.BLUE}| {Fore.YELLOW}{"Half":<10}{Fore.BLUE}| {Fore.YELLOW}{"Full":<10}{Fore.BLUE}| {Fore.YELLOW}{'Stock'} {Fore.BLUE}|"
                )
                print(Fore.BLUE + "-" * 60)

                for item in items:
                    if item["half"]:
                        half = f"₹{item['half']}"
                    else:
                        half = "-"

                    if item["full"]:
                        full = f"₹{item['full']}"

                    stock = item.get("inventory", 0)
                    if stock > 0:
                        stock_label = f"{Fore.GREEN}{stock}"
                    else:
                        stock_label = f"{Fore.RED}OUT"

                    print(
                        f"{Fore.BLUE}|{Fore.RESET} {item['name'].capitalize():<25}{Fore.BLUE}|{Fore.RESET} {half:<10}{Fore.BLUE}|{Fore.RESET} {full:<10}{Fore.BLUE}|{Fore.RESET} {stock_label:<10} {Fore.BLUE}|{Fore.RESET}"
                    )
                print(Fore.BLUE + "=" * 60)
        except Exception as e:
            display_menu_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "display_menu",
            }
            Filemode().append_data(display_menu_data,PathModel().menu_log)
            print(f"{Fore.RED}Error displaying menu: {e}")

    def search_and_order(self):
        """In this section i can search for an item or items and adds it to the cart for further process."""
        try:
            self.dislay_menu()
            search = input(
                f"\n{Fore.CYAN}Enter item name to search: {Style.RESET_ALL}"
            ).lower()
            result = []

            for category, items in self.menu.items():
                for item in items:
                    if search in item["name"].lower():
                        result.append(item)

            if not result:
                print(f"{Fore.RED}No result found!")
                return

            print(Fore.BLUE +"=" * 60)
            print(f"{Fore.CYAN}{'SEARCH RESULTS':^60}")
            print(Fore.BLUE + "=" * 60)
            print(
                f"{Fore.YELLOW}{'SN':<5}{'Name':<25}{'Half':<10}{'Full':<10}{'Stock':<9}{Fore.BLUE}║"
            )
            print(Fore.BLUE + "-" * 60)

            for SN, item in enumerate(result):
                if item["half"]:
                    half = f"₹{item["half"]}"
                else:
                    half = "-"

                if item["full"]:
                    full = f"₹{item["full"]}"

                print(
                    f"{Fore.YELLOW}{(SN+1.):<5}{Fore.RESET}{item["name"].capitalize():<25}{half:<10}{full:<10}{item['inventory']:<9}{Fore.BLUE}║"
                )
                print(Fore.BLUE + "-" * 60)

            choice = input(
                f"\n{Fore.CYAN} Select item to add (or press 'Enter' to cancel): {Style.RESET_ALL}"
            )
            if choice.isdigit() and 1 <= int(choice) <= len(result):
                selected = result[int(choice) - 1]

                if selected["inventory"] <= 0:
                    print(
                        f"{Fore.RED}SORRY: {selected['name'].capitalize()} is currently out of stock!"
                    )
                    return

                size = "f"
                price = 0
                portion = ""

                if selected["half"] != "-":
                    size = input(
                        f"{Fore.CYAN}choose size for {selected['name']}(h/f): {Style.RESET_ALL}"
                    ).lower()
                else:
                    print(f"only 'Full' size avilable for {selected['name']}")

                if size == "h" and selected["half"]:
                    price = selected["half"]
                    portion = "Half"
                else:
                    price = selected["full"]
                    portion = "Full"

                quantity_input = input(
                    f"Enter Quantity (Available: {selected['inventory']}): {Style.RESET_ALL}"
                )
                if quantity_input.isdigit() and int(quantity_input) > 0:
                    qty = int(quantity_input)

                    if qty > selected["inventory"]:
                        print(
                            f"{Fore.RED}FAILED: Only {selected['inventory']} units left in stock."
                        )
                        return
                    selected["inventory"] -= qty

                    order_item = {
                        "name": selected["name"],
                        "portion": portion,
                        "price": price,
                        "qty": qty,
                        "total": price * qty,
                    }

                    self.cart.append(order_item)
                    print(
                        f"{Fore.GREEN}SUCCESS: Added {qty} x {portion} {selected['name']} to Cart."
                    )
                else:
                    print(f"{Fore.RED}Invalid quantity. Action cancelled.")
            else:
                print(f"{Fore.YELLOW}Action Cancelled!")
        except Exception as e:
            search_and_order_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "search_and_order",
            }
            Filemode().append_data(search_and_order_data,PathModel().menu_log)
            print(f"{Fore.RED}Error in search/order: {e}")

    def view_cart(self):
        """here i am Displaying the Status of Cart"""
        try:
            if not self.cart:
                print(f"{Fore.YELLOW}Your Cart is Empty. ☹")
                return

            print("\n" + Fore.BLUE + "=" * 52)
            print(f"{Fore.YELLOW}{'YOUR CART':^52}")
            print(Fore.BLUE + "=" * 52)
            print(
                f"{Fore.CYAN}{'Item':<20}{'Size':<10}{'Qty':<5}{'Price':<7}{'Total':<10}"
            )
            print(Fore.BLUE + "-" * 52)

            grand_total = 0
            for item in self.cart:
                print(
                    f"{Fore.WHITE}{item['name'].capitalize():<20}{item['portion']:<10}{item['qty']:<5}₹{item['price']:<7}₹{item['total']:<10}"
                )
                grand_total += item["total"]

            print(Fore.BLUE + "-" * 52)
            print(f"{Fore.GREEN}{'GRAND TOTAL:':<35}₹{grand_total}")
            print(Fore.BLUE + "=" * 52)
            print(f"{Fore.YELLOW}{'\U0001f60b'*3:^52}")
        except Exception as e:
            view_cart_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_cart",
            }
            Filemode().append_data(view_cart_data,PathModel().staff_log)
            print(f"{Fore.RED}Error viewing cart: {e}")

    def cancel_order(self):
        """Function to remove item from the cart or clear cart entirely. i have kept it inside veiw cart and then the ooptions to operate various functions."""

        try:
            if not self.cart:
                print(f"{Fore.YELLOW}Cart is empty there is nothing to Cancel!")
                return

            self.view_cart()
            print(f"{Fore.YELLOW}Select Option: ")
            print(f"{Fore.MAGENTA}1. Remove a particular item")
            print(f"{Fore.MAGENTA}2. Clear Cart")
            print(f"{Fore.MAGENTA}3. Go Back")
            
            choice = int(input(f"{Fore.CYAN}Enter Your Choice: {Style.RESET_ALL}"))

            if choice == 1:
                item_no = input(f"{Fore.CYAN}Enter the Serial Number to remove item: {Style.RESET_ALL}")
                if item_no.isdigit() and 1 <= int(item_no) <= len(self.cart):
                    removed_item = self.cart.pop(int(item_no) - 1)

                    for category in self.menu.values():
                        for item in category:
                            if item["name"] == removed_item["name"]:
                                item["inventory"] += removed_item["qty"]
                                break

                    print(
                        f"{Fore.GREEN}SUCESS:{removed_item['name']} removed from cart and stock restored"
                    )
                else:
                    print(f"{Fore.RED}Invalid Serial Number!")
            elif choice == 2:
                confirm = input(
                    f"{Fore.YELLOW}are you sure, you want to clear the entire cart? (y/n): "
                ).lower()
                if confirm == "y":
                    for cart_item in self.cart:
                        for category in self.menu.values():
                            for menu_item in category:
                                if menu_item["name"] == cart_item["name"]:
                                    menu_item["inventory"] += cart_item["qty"]

                    self.cart.clear()
                    print(f"{Fore.GREEN}Your cart is cleared suceesfull.")
                else:
                    print(f"{Fore.YELLOW}Action Cancelled.")
            elif choice==3:
                print(f"{Fore.WHITE}Returning to previous menu...")
        except Exception as e:
            cancel_order_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "cancel_order",
            }
            Filemode().append_data(cancel_order_data,PathModel().order_log)
            print(f"{Fore.RED}Error canceling order: {e}")

    def update_menu(self):
        try:
            staff_subheading("UPDATE MENU")

            category = input(f"{Fore.CYAN}Enter Category : {Style.RESET_ALL}").lower().strip()

            name = input(f"{Fore.CYAN}Enter Item Name: {Style.RESET_ALL}").lower()

            
            half_input = input(f"{Fore.CYAN}Half Price (leave blank if N/A): {Style.RESET_ALL}")
            if half_input.strip():
                half = float(half_input)
            else:
                half = "-"

            full = float(input(f"{Fore.CYAN}Full Price: {Style.RESET_ALL}"))
            stock = int(input(f"{Fore.CYAN}Enter Initial Stock/Inventory: {Style.RESET_ALL}"))

            if category not in self.menu:
                self.menu[category] = []

            updated = False
            for item in self.menu[category]:
                if item["name"] == name:
                    item["half"] = half
                    item["full"] = full
                    item["inventory"] = stock
                    updated = True
                    break

            if not updated:
                self.menu[category].append(
                    {"name": name, "half": half, "full": full, "inventory": stock}
                )

            Filemode().save_data(self.menu, PathModel().menu_data)

            print(f"{Fore.GREEN}SUCCESS: {name.capitalize()} updated with {stock} units!")
        except Exception as e:
            update_menu_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "update_menu",
            }
            Filemode().append_data(update_menu_data,PathModel().menu_log)
            print(f"{Fore.RED}An unexpected error occurred: {e}")
            


    def delete_from_menu(self):
        """Permanently delete an item from the menu and save to JSON."""
        try:
            # sub_heading(f"{Fore.YELLOW}DELETE ITEMS")
            staff_subheading("DELETE ITEMS")

            category_input = input(f"{Fore.CYAN}Enter Category: {Style.RESET_ALL}").strip().lower()

            target_category = None
            for cat in self.menu.keys():
                if cat.lower() == category_input:
                    target_category = cat
                    break

            if not target_category:
                print(f"{Fore.RED}Error: Category '{category_input}' not found!")
                return

            name_to_delete = input(f"{Fore.CYAN}Enter Name to delete: {Style.RESET_ALL}").strip().lower()
            original_count = len(self.menu[target_category])

            temp_list = [
                item
                for item in self.menu[target_category]
                if item["name"].lower() != name_to_delete
            ]

            self.menu[target_category] = temp_list

            if len(self.menu[target_category]) < original_count:
                print(f"{Fore.GREEN}SUCCESS: '{name_to_delete.capitalize()}' removed from menu.")

                if not self.menu[target_category]:
                    print(
                        f"{Fore.MAGENTA}Notice: Category '{target_category}' is now empty and has been removed."
                    )
                    del self.menu[target_category]

                Filemode().save_data(self.menu, PathModel().menu_data)
            else:
                print(
                    f"{Fore.RED}Item '{name_to_delete}' not found in the '{target_category}' category."
                )
        except Exception as e:
            delete_menu_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "delete_from_menu",
            }
            Filemode().append_data(delete_menu_data,PathModel().menu_log)
            print(f"{Fore.YELLOW}An error occurred during deletion: {e}")


    def update_inventory_only(self):
        """Quickly restock an existing item."""
        try:
            staff_subheading("UPDATE INVENTORY")
            search = input(f"\n{Fore.CYAN}Enter item name to restock: {Style.RESET_ALL}").lower().strip()
            
            if not search:
                print(f"{Fore.RED}Search cannot be empty.")
                return
            
            found = False
            for category, items in self.menu.items():
                for item in items:
                    if search == item["name"].lower():
                        try:
                            current_stock = item.get('inventory', 0)
                            print(f"{Fore.WHITE}Item Found: {Fore.GREEN}{item['name'].title()}")
                            print(f"{Fore.WHITE}Current Stock: {Fore.YELLOW}{current_stock}")
                            add_stock_raw = input(f"{Fore.CYAN}Add how many units? {Style.RESET_ALL}")
                            
                            if not add_stock_raw.isdigit():
                                raise ValueError("Stock must be a positive whole number.")
                                
                            add_stock = int(add_stock_raw)
                            item["inventory"] = current_stock + add_stock
                            Filemode().save_data(self.menu, PathModel().menu_data)
                            print(
                                f"{Fore.GREEN}SUCCESS: New stock for {item['name']} is {item['inventory']}."
                            )
                            found = True
                            break
                        except ValueError as ve:
                            print(f"{Fore.RED}Invalid input: {ve}")
                            return
                    if found:
                        break
            if not found:
                print(f"{Fore.RED}Error: Item '{search}' not found in menu.")
        except Exception as e:
            inventory_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "update_invetory_only",
            }
            Filemode().append_data(inventory_data,PathModel().menu_log)
            print(f"{Fore.RED}An unexpected error occurred during inventory update: {e}")


    def payment_method(self):
        try:
            print(Fore.BLUE + "\n" + "-" * 52)
            print(f"{Fore.YELLOW}{'CHOOSE PAYMENT METHOD':^52}")
            print(Fore.BLUE + "-" * 52)
            print(f"{Fore.WHITE}1. Cash\n2. UPI\n3. Card\n4. Net Banking\n5. Return")

            select = ""
            while True:
                choice = Validator().validoption(1, 5)
                if choice == 1:
                    select = "Cash"
                elif choice == 2:
                    select = "UPI"
                elif choice == 3:
                    select = "Debit/Credit Card"
                elif choice == 4:
                    select = "Net Banking"
                else:
                    print(f"{Fore.RED}Invalid Selection, Please Try Again.")

                return select
        except Exception as e:
            payment_method_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "payment_method",
            }
            Filemode().append_data(payment_method_data,PathModel().staff_log)
            print(f"{Fore.RED}Error payment method: {e}")

    def view_bill(self):
        try:
            if not self.cart:
                print(f"{Fore.RED}There is nothing to Generate Bill.")
                return

            payment_mode = self.payment_method()
            now = datetime.now()

            print("\n")
            print(f"\n{Fore.GREEN}{'='*60}")
            print(f"{Fore.WHITE}{'INVOICE':^60}")
            print(f"\n{Fore.GREEN}{'='*60}")
            print(f"{Fore.CYAN}Date: {now.strftime('%d-%m-%Y')}")
            print(f"{Fore.CYAN}Time: {now.strftime('%H:%M:%S')}")
            print(f"{Fore.CYAN}Mode: {payment_mode}")
            print(Fore.BLUE + "-" * 60)

            sub_total = 0
            gst_rate = 0.05

            for item in self.cart:
                print(
                    f"{Fore.WHITE}{item['qty']} x {item['name']} ({item['portion']}): Rs.{item['total']}"
                )
                sub_total += item["total"]

            gst_amount = sub_total * gst_rate
            grand_total = sub_total + gst_amount

            print(Fore.BLUE + "-" * 60)
            print(f"{Fore.WHITE}{'Sub Total:':<40} Rs.{sub_total}")
            print(f"{Fore.WHITE}{'GST(5%):':<40} {gst_amount}")
            print(Fore.BLUE + "-" * 60)
            print(f"{Fore.WHITE}{'Grand Total:':<40} Rs.{grand_total}")
            print(Fore.BLUE + "-" * 60)
            print(f"{Fore.GREEN}{'THANK YOU! VISIT AGAIN':^52}")
            print(f"{Fore.GREEN}{'='*60}")

            new_order = {
                "date": now.strftime("%Y-%m-%d %H:%M:%S"),
                "items": self.cart.copy(),
                "bill_amount": grand_total,
                "payment": payment_mode,
            }
            self.order_history.append(new_order)
            Filemode().save_data(self.order_history, PathModel().order_data)

            self.cart.clear()
            print(f"{Fore.YELLOW}Transaction Complete. Thank you!")
        except Exception as e:
            view_bill_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_bill",
            }
            Filemode().append_data(view_bill_data,PathModel().staff_log)
            print(f"{Fore.RED}Error generating bill: {e}")

    def View_oreder_history(self):
        try:
            # sub_heading(f"{Fore.YELLOW}ORDER HISTORY")
            staff_subheading("ORDER HISTORY")
            if not self.order_history:
                print(f"{Fore.RED}No past orders found.")
                return
            for i, order in enumerate(self.order_history, 1):
                print(f"\n{Fore.CYAN}Order {i} | Date: {order['date']}")
                print(f"{Fore.WHITE}Payment: {order['payment']} | Total: ₹{order['bill_amount']}")
                print(Fore.BLUE + "-" * 80)
                for item in order["items"]:
                    print(f"{Fore.LIGHTWHITE_EX}{item['name']} ({item['portion']}) x {item['qty']}")
                print(Fore.BLUE + "=" * 80)
        except Exception as e:
            view_order_history_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_order_history",
            }
            Filemode().append_data(view_order_history_data,PathModel().order_log)
            print(f"{Fore.RED}Error viewing history: {e}")


def staff_dashboard():
    try:
        menu = Menu()
        while True:
            canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
            full_text = f"USERS TERMINAL :  {canvas_fore}"

            print("\n" + Fore.BLUE + "╔" + "═" * 78 + "╗")
            print(f"{Fore.BLUE}║{Fore.YELLOW}{full_text:>94}{Fore.BLUE}{'║':>24}")
            print(Fore.BLUE +"╠" + "═" * 78 + "╣")
            options = [
                "View Menu",
                "Search & Add to Cart",
                "View Cart",
                "Cancel Order",
                "Table Management",
                "View Invoice & Checkout",
                "Order History",
                "View Staff Profile",
                "Back",
            ]
            for i, opt in enumerate(options, 1):
                print(f"{Fore.BLUE}║{Fore.YELLOW}{i:>3}. {Fore.WHITE}{opt:73}{Fore.BLUE}║")

            print(Fore.BLUE + "╚" + "═" * 78 + "╝")

            choice = Validator().validoption(1, 9)

            if choice == 1:
                menu.dislay_menu()
            elif choice == 2:
                menu.search_and_order()
            elif choice == 3:
                menu.view_cart()
            elif choice == 4:
                menu.cancel_order()
            elif choice == 5:
                TableManager().table_dashboard()
            elif choice == 6:
                menu.view_bill()
            elif choice == 7:
                menu.View_oreder_history()
            elif choice == 8:
                User().view_staff()
            elif choice == 9:
                break

            if choice not in [4,5, 9]:
                input(f"\n{Fore.LIGHTYELLOW_EX}Press [Enter] to return to Dashboard...")
    except Exception as e:
        staff_dashboard_data={
            "error": str(e),
            "time": str(datetime.now()),
            "function name": "staff_dashboard",
        }
        Filemode().append_data(staff_dashboard_data,PathModel().staff_log)
        print(f"{Fore.RED}Staff Dashboard Critical Error: {e}")


# staff_dashboard()
