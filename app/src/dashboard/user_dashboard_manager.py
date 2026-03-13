import time
from src.auth.manage_user import user_menu
from src.auth.signup_page import Signup
from src.auth.login_page import Login
from src.security.validation import Validator
from src.filehandling.filemode import Filemode

file = Filemode()
all_user = file.load_data()
valid = Validator()

def user_menu_dashobard():
    user_menu()
    while True:
        option = valid.validoption()
        if option == 1:
            admin_found = False
            for user in all_user:
                if user.get("role") == "Admin":
                    admin_found = True
                    break
            if admin_found == False:
                Signup().admin()
            else:
                Signup().staff()
        elif option == 2:
            Login().login()
        elif option == 3:
            print("Exiting", end="")
            for _ in range(5):
                time.sleep(0.25)
                print(".", end="")
            print("\nGoodbye!")
            break
        else:
            print("PLease select option carefully!")
