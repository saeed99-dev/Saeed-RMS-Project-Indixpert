from src.filehandling.filemode import Filemode
from src.model.models import PathModel
from src.utils.tools import admin_subheading,connect_subheading
from src.domain.staff_menu import Menu
from src.domain.usersdata import User
from src.security.validation import Validator
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


class Admin:
    def __init__(self):
        try:
            self.orders=Filemode().load_data(PathModel().order_data)
            self.userdata=Filemode().load_data(PathModel().user_data)
            self.menu=Filemode().load_data(PathModel().menu_data)
        except Exception as e:
            print(f"{Fore.RED}Error initializing Admin data: {e}")


    def analyze_reports(self):
        """Calculates total revenue, top items, and provides a strategy summary."""
        try:
            admin_subheading("SALES ANALYSIS & STRATEGY")
            if not self.orders:
                print(f"{Fore.RED}No sales data available for analysis.")
                return

            total_revenue = sum(order.get("bill_amount", 0) for order in self.orders)
            total_orders = len(self.orders)

            print(f"{Fore.CYAN}Total Revenue: {Fore.WHITE}₹{total_revenue:,.2f}")
            print(f"{Fore.CYAN}Total Transactions: {Fore.WHITE}{total_orders}")
            print(f"{Fore.CYAN}Average Order Value: {Fore.WHITE}₹{(total_revenue/total_orders):,.2f}")

            print(f"\n{Fore.GREEN}--- DETAIL STRATEGY ---")
            if total_revenue < 5000:
                print(
                    f"{Fore.MAGENTA}Strategy: Low Volume. Suggesting 'Happy Hour' discounts or social media promotion."
                )
            else:
                print(
                    f"{Fore.GREEN}Strategy: Healthy Volume. Suggesting 'Loyalty Program' to retain high-value customers."
                )

            input(f"\n{Fore.YELLOW}Press [Enter] to return...")
        except Exception as e:
            analyze_reports_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "analyse_reports",
            }
            Filemode().append_data(analyze_reports_data,PathModel().admin_log)
            print(f"{Fore.RED}An error occurred during analysis: {e}")

    def manage_menu(self):
        
        
        while True:
            try:
                connect_subheading("MENU MANAGEMENT")
                options = [
                "View Food Menu Item",
                "Add/Update Menu Item",
                "Delete Menu Item",
                "Update Inventory Only",
                "Back"
                ]
                for i, opt in enumerate(options, 1):
                    print(f"{Fore.BLUE}║{Fore.YELLOW}{i:>3}. {Fore.WHITE}{opt:73}{Fore.BLUE}║")

                print(Fore.BLUE + "╚" + "═" * 78 + "╝")

                choice = Validator().validoption(1,5)

                if choice == 1:
                    Menu().dislay_menu()
                    input(f"{Fore.YELLOW}Press [Enter] to go Back ")
                elif choice == 2:
                    Menu().update_menu()
                elif choice == 3:
                    Menu().delete_from_menu()
                elif choice == 4:
                    Menu().update_inventory_only()
                elif choice == 5:
                    break
            except Exception as e:
                manage_menu_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "manage_menu",
                }
                Filemode().append_data(manage_menu_data,PathModel().admin_log)
                print(f"{Fore.RED}Menu Management Error: {e}")


    def manage_staff(self):
        
        
        while True:
            try:
                connect_subheading("USERS MANAGEMENT")
                options = [
                "View All Staff",
                "View Admin",
                "View Blocked Users",
                "Block/Unblock Staff",
                "Create Admin",
                "View Particular User Profile",
                "Back"
                ]
                for i, opt in enumerate(options, 1):
                    print(f"{Fore.BLUE}║{Fore.YELLOW}{i:>3}. {Fore.WHITE}{opt:73}{Fore.BLUE}║")

                print(Fore.BLUE + "╚" + "═" * 78 + "╝")

                choice = Validator().validoption(1,7)

                if choice == 1:
                    User().view_staff()
                elif choice ==2:
                    User().view_admin()
                elif choice == 3:
                    User().view_blocked_profile()
                elif choice == 4:
                    User().block_unblock_profile()
                elif choice == 5:
                    User().promote_staff_to_admin()
                elif choice==6:
                    User().view_member_profile()
                elif choice==7:
                    break

                if choice !=7:
                    input(f"{Fore.YELLOW}Press [Enter] to go Back ")
            except Exception as e:
                manage_staff_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "manage_staff",
                }
                Filemode().append_data(manage_staff_data,PathModel().admin_log)
                print(f"{Fore.RED}Staff Management Error: {e}")



def admin_interface():
    """Primary Admin Dashboard entry point."""
    try:
        admin = Admin()
        while True:
            canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
            full_text = f"{'A D M I N   T E R M I N A L'} :  {canvas_fore}"
            print("\n" + Fore.YELLOW + "╔" + "═" * 78 + "╗")
            print(f"{Fore.YELLOW}{'║':<18}{Fore.MAGENTA}{full_text}{Fore.YELLOW}{'║':>16}")
            print(Fore.YELLOW +"╠" + "═" * 78 + "╣")
            options = [
                "Analyse Report and Strategy",
                "Staff Management",
                "Menu Management",
                "View Order History",
                "Back"
                ]
            for i, opt in enumerate(options, 1):
                    print(f"{Fore.YELLOW}║{Fore.CYAN}{i:>3}. {Fore.WHITE}{opt:73}{Fore.YELLOW}║")

            print(Fore.YELLOW + "╚" + "═" * 78 + "╝")

            choice = Validator().validoption(1,5)

            if choice == 1:
                admin.analyze_reports()
            elif choice == 2:
                admin.manage_staff()
            elif choice == 3:
                admin.manage_menu()
            elif choice==4:
                Menu().View_oreder_history()
            elif choice==5:
                print(f"{Fore.GREEN}Logging out from Admin Dashboard...")
                break
    except Exception as e:
        admin_inteface_data={
            "error": str(e),
            "time": str(datetime.now()),
            "function name": "admin_inteface",
        }
        Filemode().append_data(admin_inteface_data,PathModel().admin_log)
        print(f"{Fore.RED}Critical Interface Error: {e}")
