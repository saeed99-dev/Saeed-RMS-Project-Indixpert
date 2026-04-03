from src.filehandling.filemode import Filemode
from src.model.models import PathModel
from src.utils.tools import sub_heading


class User:
    def __init__(self):
        self.users = Filemode().load_data(PathModel().user_data)

    def view_staff(self):
        sub_heading("STAFF PROFILE DIRECTORY : [C A N V A S]")

        print(
            f"{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}"
        )
        print("-" * 80)

        staff_found = False
        for user in self.users:
            if user["role"] == "Staff":
                print(
                    f"{user['id']:<10} | {user['name']:<10} | {user['role']:<8} | {user['email']:<20} | {user['mobile']:<10}"
                )
                print("-" * 80)
                staff_found = True

        if not staff_found:
            print(f"{'No Staff Member Found':^60}")
            print("-" * 80)

        print("=" * 80)

    def view_admin(self):
        sub_heading("ADMIN PROFILE DIRECTORY : [C A N V A S]")
        print(
            f"{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}"
        )
        print("-" * 80)

        admin_found = False
        for user in self.users:
            if user["role"] == "Admin":
                print(
                    f"{user['id']:<10} | {user['name']:<10} | {user['role']:<8} | {user['email']:<20} | {user['mobile']:<10}"
                )
                print("-" * 80)
                admin_found = True

        if not admin_found:
            print(f"{'No Admin Member Found':^60}")
            print("-" * 80)

        print("=" * 80)

    def view_blocked_profile(self):
        sub_heading("BLOCKED PROFILE DIRECTORY : [C A N V A S]")

        print(
            f"{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}"
        )
        print("-" * 80)

        blocked_found = False
        for user in self.users:
            if user["role"] == "Blocked":
                print(
                    f"{user['id']:<10} | {user['name']:<10} | {user['role']:<8} | {user['email']:<20} | {user['mobile']:<10}"
                )
                print("-" * 80)
                blocked_found = True

        if not blocked_found:
            print(f"{'No Blocked Member Found':^60}")
            print("-" * 80)

        print("=" * 80)

    def block_unblock_profile(self):

        sub_heading("MANAGE ROLE : [C A N V A S]")

        input_user_id = input("Please Enter user ID: ")

        found = False
        for user in self.users:
            if user["id"] == input_user_id:
                found = True

                is_blocked = user.get("role") == "Blocked"
                action = "unblock" if is_blocked else "block"
                new_role = "User" if is_blocked else "Blocked"

                confirm = input(
                    f"Are you sure you want to {action} user {input_user_id}? (y/n): "
                ).lower()

                if confirm == "y":
                    user["role"] = new_role

                    Filemode().save_data(self.users, PathModel().user_data)
                else:
                    print("\nOperation cancelled.")

                break

        if not found:
            print(f"User with ID {input_user_id} not found in the data")


    def promote_staff_to_admin(self):

        sub_heading("PROMOTE ROLE : [C A N V A S]")

        input_user_id = input("Please Enter user ID to promote: ")
        
        found = False
        for user in self.users:
            if user["id"] == input_user_id:
                found = True
                
                current_role = user.get('role', '')
                
                if current_role == "Admin":
                    print(f"User {input_user_id} is already an Admin.")
                elif current_role != "Staff":
                    print(f"Promotion Denied: User is currently '{current_role}'.")
                    print("Only users with 'Staff' role can be promoted to Admin here.")
                else:
                    print(f"\nTarget User Found: {user.get('name', 'N/A')} (Current Role: Staff)")
                    confirm = input(f"Confirm promotion of ID {input_user_id} to Admin? (y/n): ").lower()
                    
                    if confirm == 'y':
                        user['role'] = "Admin"
                        
                        Filemode().save_data(self.users,PathModel().user_data)
                    else:
                        print("\nPromotion cancelled by administrator.")
                
                break
                
        if not found:
            error_msg = f"User ID {input_user_id} not found in the system"
            print(f"{error_msg:^60}")

    def view_member_profile(self):

        sub_heading("VIEW MEMBER PROFILE : [C A N V A S]")
        
        input_user_id = input("Please Enter User ID: ")
        
        found = False
        for user in self.users:
            if user["id"] == input_user_id:
                found = True
                
                print("\n" + "="*30)
                print(f"MEMBER DETAILS FOR ID: {input_user_id}")
                print("="*30)
                print(f"{'Name:':<15} {user.get('name', 'N/A')}")
                print(f"{'Role:':<15} {user.get('role', 'N/A')}")
                print(f"{'Email:':<15} {user.get('email', 'N/A')}")
                
                status = "Blocked" if user.get('role') == "Blocked" else "Active"
                print(f"{'Status:':<15} {status}")
                print("="*30)
                
                break
        
        if not found:
            error_msg = f"User ID {input_user_id} not found in the system"
            print(f"\n{error_msg:^60}")