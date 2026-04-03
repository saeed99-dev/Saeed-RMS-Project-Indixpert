from src.filehandling.filemode import Filemode
from src.model.models import PathModel
from src.utils.tools import sub_heading
from src.domain.staff_menu import Menu
from src.domain.usersdata import User
from src.security.validation import Validator


class Admin:
    def __init__(self):
        self.orders=Filemode().load_data(PathModel().order_data)
        self.userdata=Filemode().load_data(PathModel().user_data)
        self.menu=Filemode().load_data(PathModel().menu_data)

    def analyze_reports(self):
        """Calculates total revenue, top items, and provides a strategy summary."""
        sub_heading("SALES ANALYSIS & STRATEGY")
        if not self.orders:
            print("No sales data available for analysis.")
            return

        total_revenue = sum(order.get("bill_amount", 0) for order in self.orders)
        total_orders = len(self.orders)

        print(f"Total Revenue: ₹{total_revenue:,.2f}")
        print(f"Total Transactions: {total_orders}")
        print(f"Average Order Value: ₹{(total_revenue/total_orders):,.2f}")

        print("\n--- DETAIL STRATEGY ---")
        if total_revenue < 5000:
            print(
                "Strategy: Low Volume. Suggesting 'Happy Hour' discounts or social media promotion."
            )
        else:
            print(
                "Strategy: Healthy Volume. Suggesting 'Loyalty Program' to retain high-value customers."
            )

        input("\nPress [Enter] to return...")

    def manage_menu(self):
        
        
        while True:
            print("\n" + "╔" + "═" * 78 + "╗")
            print(f"║{'MENU MANAGEMENT : [C A N V A S]':^78}║")
            print("╠" + "═" * 78 + "╣")
            print(f"║ {'1. View Food Menu Item':76} ║")
            print(f"║ {'2. Add/Update Menu Item':76} ║")
            print(f"║ {'3. Delete Menu Item':76} ║")
            print(f"║ {'4. Update Inventory Only':76} ║")
            print(f"║ {'5. Back':76} ║")
            print("╚" + "═" * 78 + "╝")

            choice = Validator().validoption(1,5)

            if choice == 1:
                Menu().dislay_menu()
                input("Press [Enter] to go Back ")
            elif choice == 2:
                Menu().update_menu()
            elif choice == 3:
                Menu().delete_from_menu()
            elif choice == 4:
                Menu().update_inventory_only()
            elif choice == 5:
                break
            else:
                print("Invalid Selection! Please choose between 1-5.")

    def manage_staff(self):
        
        
        while True:
            print("\n" + "╔" + "═" * 78 + "╗")
            print(f"║{'USERS MANAGEMENT : [C A N V A S]':^78}║")
            print("╠" + "═" * 78 + "╣")
            print(f"║ {'1. View All Staff':76} ║")
            print(f"║ {'2. View Admin':76}║")
            print(f"║ {'3. View Blocked Users':76} ║")
            print(f"║ {'4. Block/Unblock Staff':76} ║")
            print(f"║ {'5. Create Admin':76} ║")
            print(f"║ {'6. View Particular User Profile':76} ║")
            print(f"║ {'7. Back':76} ║")
            print("╚" + "═" * 78 + "╝")

            choice = Validator().validoption(1,7)

            if choice == 1:
                User().view_staff()
                input("Press [Enter] to go Back ")
            elif choice ==2:
                User().view_admin()
                input("Press [Enter] to go Back ")
            elif choice == 3:
                User().view_blocked_profile()
                input("Press [Enter] to go Back ")
            elif choice == 4:
                User().block_unblock_profile()
                input("Press [Enter] to go Back ")
            elif choice == 5:
                User().promote_staff_to_admin()
                input("Press [Enter] to go Back ")
            elif choice==6:
                User().view_member_profile()
                input("Press [Enter] to go Back ")
            elif choice==7:
                break
            else:
                print("Invalid Selection! Please choose between 1-7.")



def admin_interface():
    """Primary Admin Dashboard entry point."""
    admin = Admin()

    while True:
        print("\n" + "╔" + "═" * 78 + "╗")
        print(f"║{'A D M I N   T E R M I N A L : [C A N V A S]':^78}║")
        print("╠" + "═" * 78 + "╣")
        print(f"║ {'1. Analyse Report and Strategy':77}║")
        print(f"║ {'2. Staff Management':77} ║")
        print(f"║ {'3. Menu Management':77} ║")
        print(f"║ {'4. View Order History':77} ║")
        print(f"║ {'5. Logout':77} ║")
        print("╚" + "═" * 78 + "╝")

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
            print("Logging out from Admin Dashboard...")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

