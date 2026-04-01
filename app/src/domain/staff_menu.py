from datetime import datetime
from src.model.models import PathModel
from src.filehandling.filemode import Filemode
from src.utils.tools import sub_heading
from src.domain.usersdata import User
from src.domain.table_menu import TableManager


class Menu:
    def __init__(self):
        self.cart=[]
        self.menu=Filemode().load_data(PathModel().menu_data)
        self.order_history=Filemode().load_data(PathModel().order_data)


    def dislay_menu(self):
        sub_heading("RESTAURANT MENU")

        for category, items in self.menu.items():
            print(f"\n{category.upper()}")
            print("-" * 52)
            print(f"| {"Name":<25}| {"Half":<10}| {"Full":<10}|")
            print("-" * 52)

            for item in items:
                if item["half"]:
                    half = f"₹{item['half']}"
                else:
                    half = "-"

                if item["full"]:
                    full = f"₹{item['full']}"

                print(f"| {item["name"].capitalize():<25}| {half:<10}| {full:<10}|")
            print("=" * 52)

    def search_and_order(self):
        """In this section i can search for an item or items and adds it to the cart for further process."""
        self.dislay_menu()
        search = input("\nEnter item name to search: ").lower()
        result = []

        for category, items in self.menu.items():
            for item in items:
                if search in item["name"].lower():
                    result.append(item)

        if not result:
            print("No result found!")
            return

        print("\n" + "=" * 52)
        print(f"{'SEARCH RESULTS':>32}")
        print("=" * 52)
        print("-" * 52)
        print(f"{"SN":<5}{"Name":<25}{"Half":<10}{"Full":<10}")
        print("-" * 52)

        for SN, item in enumerate(result):
            if item["half"]:
                half = f"₹{item["half"]}"
            else:
                half = "-"

            if item["full"]:
                full = f"₹{item["full"]}"

            print(f"{(SN+1):<5}{item["name"].capitalize():<25}{half:<10}{full:<10}")

        choice = input("\n Select item to add (or press 'Enter' to cancel): ")
        if choice.isdigit() and 1 <= int(choice) <= len(result):
            selected = result[int(choice) - 1]

            size = "f"
            price = 0
            portion = ""

            if selected["half"] != "-":
                size = input(f"choose size for {selected['name']}(h/f): ").lower()
            else:
                print(f"only 'Full' size avilable for {selected['name']}")

            if size == "h" and selected["half"]:
                price = selected["half"]
                portion = "Half"
            else:
                price = selected["full"]
                portion = "Full"

            quantity_input = input("Enter Quantity: ")
            if quantity_input.isdigit() and int(quantity_input) > 0:
                qty = int(quantity_input)

                order_item = {
                    "name": selected["name"],
                    "portion": portion,
                    "price": price,
                    "qty": qty,
                    "total": price * qty,
                }
                self.cart.append(order_item)
                print(f"SUCCESS: Added {qty} x {portion} {selected['name']} to Cart.")
            else:
                print("Invalid quantity. Action cancelled.")
        else:
            print("Action Cancelled!")

    def view_cart(self):
        """here i am Displaying the Status of Cart"""
        if not self.cart:
            print("Your Cart is Empty. ☹")
            return

        print("\n" + "=" * 52)
        print(f"{'YOUR CART':^52}")
        print("=" * 52)
        print(f"{'Item':<20}{'Size':<10}{'Qty':<5}{'Price':<7}{'Total':<10}")
        print("-" * 52)

        grand_total = 0
        for item in self.cart:
            print(
                f"{item['name'].capitalize():<20}{item['portion']:<10}{item['qty']:<5}₹{item['price']:<7}₹{item['total']:<10}"
            )
            grand_total += item["total"]

        print("-" * 52)
        print(f"{'GRAND TOTAL:':<35}₹{grand_total}")
        print("=" * 52)
        print(f"{'\U0001f60b'*3:^52}")

    def cancel_order(self):
        """Function to remove item from the cart or clear cart entirely. i have kept it inside veiw cart and then the ooptions to operate various functions."""

        if not self.cart:
            print("\nCart is empty there is nothing to Cancel!")
            return

        self.view_cart()
        print("Select Option: ")
        print("1. Remove a particular item")
        print("2. Clear Cart")
        print("3. Go Back")

        choice = input("\n Enter Your Choice: ")

        if choice == "1":
            item_no = input("Enter the Serial Number to remove item: ")
            if item_no.isdigit() and 1 <= int(item_no) <= len(self.cart):
                removed_item = self.cart.pop(int(item_no) - 1)
                print(f"SUCESS:{removed_item['name']} removed from cart")
            else:
                print("Invalid Serial Number!")
        elif choice == "2":
            confirm = input(
                "are you sure, you want to clear the entire cart? (y/n): "
            ).lower()
            if confirm == "y":
                self.cart.clear()
                print("Your cart is cleared suceesfull.")
            else:
                print("Action Cancelled.")
        else:
            print("Returning to Menu...")

    def update_menu(self):
        print("\n--- Update Menu ---")
        category = input("Enter Category : ").lower()
        name = input("Enter Item Name: ").lower()

        try:
            half_input = input("Half Price (leave blank if N/A): ")
            if half_input.strip():
                half = float(half_input)
            else:
                half = "-"

            full = float(input("Full Price: "))

            if category not in self.menu:
                self.menu[category] = []

            updated = False
            for item in self.menu[category]:
                if item["name"] == name:
                    item["half"] = half
                    item["full"] = full
                    updated = True
                    break

            if not updated:
                self.menu[category].append({"name": name, "half": half, "full": full})
            
            Filemode().save_data(self.menu,PathModel().menu_data)

            print("Menu updated and Saved successfully!")
        except Exception as e:
            print(e)

    def payment_method(self):
        print("\n" + "-" * 52)
        print(f"{'CHOOSE PAYMENT METHOD':^52}")
        print("-" * 52)
        print("1. Cash")
        print("2. UPI (Phonepay/Gpay/Paytm)")
        print("3. Debit/Credit Card")
        print("4. Net Banking")
        print("5. Return Back")

        select = ""
        while True:
            choice = int(input("\n Select Payment Option(1-5): "))
            if choice == 1:
                select = "Cash"
            elif choice == 2:
                select = "UPI"
            elif choice == 3:
                select = "Debit/Credit Card"
            elif choice == 4:
                select = "Net Banking"
            else:
                print("Invalid Selection, Please Try Again.")

            return select

    def view_bill(self):
        if not self.cart:
            print("\nThere is nothing to Generate Bill.")
            return

        payment_mode = self.payment_method()
        now = datetime.now()

        print("\n")
        print("=" * 60)
        print(f"{'Your Bill':^52}")
        print("=" * 60)
        print(f"Date: {now.strftime('%d-%m-%Y')}")
        print(f"Time: {now.strftime('%H:%M:%S')}")
        print(f"Payment Method/Mode: {payment_mode}")
        print("-" * 60)

        sub_total = 0
        gst_rate = 0.05

        for item in self.cart:
            print(f"{item['qty']} x {item['name']} ({item['portion']}): Rs.{item['total']}")
            sub_total += item["total"]
        
        gst_amount = sub_total * gst_rate
        grand_total = sub_total + gst_amount
        
        print("-" * 52)
        print(f"{'Sub Total:':<40} Rs.{sub_total}")
        print(f"{'GST(5%):':<40} {gst_amount}")
        print("-" * 52)
        print(f"{'Grand Total:':<40} Rs.{grand_total}")
        print("-" * 52)
        print(f"{'THANK YOU! VISIT AGAIN':^52}")
        print("=" * 52)

        new_order = {
            "date": now.strftime('%Y-%m-%d %H:%M:%S'),
            "items": self.cart.copy(),
            "bill_amount": grand_total,
            "payment": payment_mode
        }
        self.order_history.append(new_order)
        Filemode().save_data(self.order_history,PathModel().order_data)
        
        self.cart.clear()

    def View_oreder_history(self):
        sub_heading('ORDER HISTORY')
        if not self.order_history:
            print("No past orders found.")
            return
        for i , order in enumerate(self.order_history,1):
            print(f"\nOrder {i} | Date: {order['date']}")
            print(f"Payment: {order['payment']} | Total: ₹{order['bill_amount']}")
            print("-" * 60)
            for item in order['items']:
                print(f"- {item['name']} ({item['portion']}) x {item['qty']}")
            print("=" * 60)

def staff_dashboard():
    menu = Menu()

    while True:
        print("\n" + "╔" + "═" * 58 + "╗")
        print(f"║{'STAFF TERMINAL : [C A N V A S]':^58}║")
        print("╠" + "═" * 58 + "╣")
        options = [
            "View Menu", 
            "Search & Order", 
            "View Cart", 
            "Cancel Order", 
            "Table Management", 
            "View Invoice & Checkout", 
            "Order History", 
            "View Staff Profile", 
            "Back"
            ]
        for i,opt in enumerate(options,1):
            print(f"║ {i}. {opt:56}║")
        
        print("╚" + "═" * 58 + "╝")

        choice=int(input("\n Select Option(1-9): "))

        if choice==1:
            menu.dislay_menu()
            input("Press [Enter] to Show the Dashboard ")
        elif choice==2:
            menu.search_and_order()
        elif choice==3:
            menu.view_cart()
        elif choice==4:
            menu.cancel_order()
        elif choice==5:
            TableManager().table_dashboard()
        elif choice==6:
            menu.view_bill()
        elif choice==7:
            menu.View_oreder_history()
        elif choice==8:
            User().view_staff_profile()
            input("Press [Enter] to Show the Dashboard ")
        elif choice==9:
            break
        else:
            print("Invalid Option!")

# staff_dashboard()

