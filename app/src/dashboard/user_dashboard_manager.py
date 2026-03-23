import time
from src.auth.manage_user import user_menu
from src.auth.signup_page import Signup
from src.auth.login_page import Login
from src.security.validation import Validator

def user_menu_dashobard():
    user_menu()
    while True:
        valid = Validator()
        option = valid.validoption()
        if option == 1:
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
            print("PLease select option carefully(option > 0)!")
