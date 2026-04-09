from src.filehandling.filemode import Filemode
from src.domain.staff_menu import staff_dashboard
from src.domain.admin_menu import admin_interface
from src.security.validation import Validator
from src.model.models import PathModel
from src.utils.tools import main_subheading
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


class Login:
    def __init__(self):
        self.userdata = Filemode().load_data(PathModel().user_data)        

    def login(self):
        valid = Validator()
        main_subheading("LOGIN PORTAL")
        try:
            while True:
                found = False
                input_email = valid.validemail()
                input_password = valid.validpassword()
                
                if not self.userdata:
                    print(f"{Fore.RED}System Error: No user database found.")
                    return None
                
                for user in self.userdata:
                    if user["email"] == input_email and user["password"] == input_password:
                        found = True
                        if user["role"] != "Blocked":
                            print(f"\n{Fore.GREEN}Login Successful! Welcome, {user.get('name', 'User')}.")

                            if user["role"] == "Admin":
                                admin_interface()
                            elif user["role"] == "Staff":
                                staff_dashboard()

                            return input_email, input_password
                        else:
                            print(f"\n{Fore.RED}Access Denied: You are Blocked! Contact Admin.")
                            return None
                if not found:
                    print(f"\n{Fore.RED}User Not Found! Please enter correct email or Password")
                    continue
        except Exception as e:
            login_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "login",
            }
            Filemode().append_data(login_data,PathModel().athu_log)
            print(f"{Fore.RED}An error: {e}. Please try again later.")
            
            return None

                
