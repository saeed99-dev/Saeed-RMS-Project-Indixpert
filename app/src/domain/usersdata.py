from src.filehandling.filemode import Filemode
from src.model.models import PathModel
from src.utils.tools import admin_subheading
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


class User:
    def __init__(self):
        self.users = Filemode().load_data(PathModel().user_data)

    def view_staff(self):
        try:
            admin_subheading("STAFF PROFILE DIRECTORY")

            print(
                f"{Fore.CYAN}{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}"
            )
            print(Fore.BLUE + "-" * 80)

            staff_found = False
            for user in self.users:
                if user.get("role") == "Staff":
                    print(
                        f"{Fore.WHITE}{user['id']:<10} | {user['name']:<10} | {Fore.GREEN}{user['role']:<8} | {Fore.WHITE}{user['email']:<20} | {user['mobile']:<10}"
                    )
                    print(Fore.BLUE + "-" * 80)
                    staff_found = True

            if not staff_found:
                print(f"{Fore.RED}{'No Staff Member Found':^60}")
                print(Fore.BLUE + "-" * 80)

            print(Fore.CYAN + "=" * 80)
        except Exception as e:
            view_staff_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_staff",
            }
            Filemode().append_data(view_staff_data,PathModel().staff_log)
            print(f"{Fore.RED}Error accessing staff directory: {e}")


    def view_admin(self):
        try:
            admin_subheading("ADMIN PROFILE DIRECTORY")
            # sub_heading(f"{Fore.YELLOW}ADMIN PROFILE DIRECTORY : [C A N V A S]")
            print(
                f"{Fore.CYAN}{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}"
            )
            print(Fore.BLUE + "-" * 80)

            admin_found = False
            for user in self.users:
                if user.get("role") == "Admin":
                    print(
                        f"{Fore.WHITE}{user['id']:<10} | {user['name']:<10} | {Fore.MAGENTA}{user['role']:<8} | {Fore.WHITE}{user['email']:<20} | {user['mobile']:<10}"
                    )
                    print(Fore.BLUE + "-" * 80)
                    admin_found = True

            if not admin_found:
                print(f"{Fore.RED}{'No Admin Member Found':^60}")
                print(Fore.BLUE + "-" * 80)

            print(Fore.CYAN + "=" * 80)
        except Exception as e:
            view_admin_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_admin",
            }
            Filemode().append_data(view_admin_data,PathModel().admin_log)
            print(f"{Fore.RED}Error accessing admin directory: {e}")


    def view_blocked_profile(self):
        try:
            admin_subheading("BLOCKED PROFILE DIRECTORY")

            print(
                f"{Fore.CYAN}{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}"
            )
            print(Fore.BLUE + "-" * 80)

            blocked_found = False
            for user in self.users:
                if user.get("role") == "Blocked":
                    print(
                        f"{Fore.WHITE}{user['id']:<10} | {user['name']:<10} | {Fore.RED}{user['role']:<8} | {Fore.WHITE}{user['email']:<20} | {user['mobile']:<10}"
                    )
                    print(Fore.BLUE + "-" * 80)
                    blocked_found = True

            if not blocked_found:
                print(f"{Fore.GREEN}{'No Blocked Member Found':^60}")
                print(Fore.BLUE + "-" * 80)

            print(Fore.CYAN + "=" * 80)
        except Exception as e:
            blocked_view_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_blocked_profile",
            }
            Filemode().append_data(blocked_view_data,PathModel().staff_log)
            print(f"{Fore.RED}Error accessing blocked directory: {e}")


    def block_unblock_profile(self):
        try:
            admin_subheading("MANAGE ROLE")

            input_user_id = input(f"{Fore.CYAN}Please Enter user ID: {Style.RESET_ALL}").strip()

            found = False
            for user in self.users:
                if user["id"] == input_user_id:
                    found = True

                    is_blocked = user.get("role") == "Blocked"
                    action = "unblock" if is_blocked else "block"
                    new_role = "User" if is_blocked else "Blocked"

                    action_color = Fore.GREEN if is_blocked else Fore.RED
                    print(f"\n{Fore.WHITE}Target User: {Fore.CYAN}{user['name']} {Fore.WHITE}(Current Role: {Fore.MAGENTA}{user['role']}{Fore.WHITE})")

                    confirm = input(
                        f"{Fore.YELLOW}Are you sure you want to {action_color}{action} {Fore.YELLOW}user {input_user_id}? (y/n): {Style.RESET_ALL}"
                    ).lower()

                    if confirm == "y":
                        user["role"] = new_role

                        Filemode().save_data(self.users, PathModel().user_data)
                        print(f"\n{Fore.GREEN}SUCCESS: User {input_user_id} is now set to '{new_role}'.")
                    else:
                        print(f"\n{Fore.YELLOW}Operation cancelled. No changes made.")
                    break

            if not found:
                print(f"{Fore.RED}User with ID {input_user_id} not found in the data")
        except Exception as e:
            unblock_profile_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "block_unblock_profile",
            }
            Filemode().append_data(unblock_profile_data,PathModel().staff_log)
            print(f"{Fore.RED}An error occurred during role management: {e}")



    def promote_staff_to_admin(self):
        try:
            admin_subheading("PROMOTE ROLE")

            input_user_id = input(f"{Fore.CYAN}Please Enter user ID to promote: {Style.RESET_ALL}").strip()
            
            found = False
            for user in self.users:
                if user["id"] == input_user_id:
                    found = True
                    
                    current_role = user.get('role', '')
                    
                    if current_role == "Admin":
                        print(f"{Fore.YELLOW}Notice: User {input_user_id} is already an Admin.")
                    elif current_role != "Staff":
                        print(f"{Fore.RED}Promotion Denied: User is currently '{current_role}'.")
                        print(f"{Fore.WHITE}Only users with 'Staff' role can be promoted to Admin here.")
                    else:
                        print(f"\n{Fore.WHITE}Target User Found: {Fore.CYAN}{user.get('name', 'N/A')} ({Fore.WHITE}Current Role: {Fore.GREEN}Staff)")

                        confirm = input(f"{Fore.YELLOW}Confirm promotion of ID {input_user_id} to {Fore.MAGENTA}Admin? {Fore.YELLOW}(y/n): {Style.RESET_ALL}").lower()
                        
                        if confirm == 'y':
                            user['role'] = "Admin"
                            
                            Filemode().save_data(self.users,PathModel().user_data)
                            print(f"\n{Fore.GREEN}SUCCESS: {user.get('name')} has been promoted to Admin.")
                        else:
                            print(f"\n{Fore.YELLOW}Promotion cancelled by administrator.")
                    
                    break
                    
            if not found:
                error_msg = f"User ID {input_user_id} not found in the system"
                print(f"{Fore.RED}{error_msg:^60}")
        except Exception as e:
            promote_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "promote_staff_to_admin",
            }
            Filemode().append_data(promote_data,PathModel().admin_log)
            print(f"{Fore.RED}An error occurred during promotion: {e}")


    def view_member_profile(self):
        
        try:
            admin_subheading("VIEW MEMBER PROFILE")
            
            input_user_id = input(f"{Fore.CYAN}Please Enter User ID: {Style.RESET_ALL}")
            
            found = False
            for user in self.users:
                if user["id"] == input_user_id:
                    found = True

                    status = "Blocked" if user.get('role') == "Blocked" else "Active"
                    status_color = Fore.RED if status == "Blocked" else Fore.GREEN
                    
                    print("\n" + Fore.BLUE + "="*35)
                    print(f"{Fore.WHITE}MEMBER DETAILS FOR ID: {input_user_id}")
                    print(Fore.BLUE + "="*35)
                    print(f"{Fore.CYAN}{'Name:':<15} {Fore.WHITE}{user.get('name', 'N/A')}")
                    print(f"{Fore.CYAN}{'Role:':<15} {Fore.MAGENTA}{user.get('role', 'N/A')}")
                    print(f"{Fore.CYAN}{'Email:':<15} {Fore.WHITE}{user.get('email', 'N/A')}")                    
                    print(f"{Fore.CYAN}{'Status:':<15} {status_color}{status}")
                    print(Fore.BLUE + "="*35)
                    break
            
            if not found:
                error_msg = f"User ID {input_user_id} not found in the system"
                print(f"\n{Fore.RED}{error_msg:^60}")
        except Exception as e:
            member_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_member_profile",
            }
            Filemode().append_data(member_data,PathModel().admin_log)
            print(f"{Fore.RED}Error viewing member profile: {e}")
