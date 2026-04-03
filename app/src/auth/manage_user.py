from src.auth.signup_page import Signup
from src.auth.login_page import Login
from src.security.validation import Validator
from src.utils.tools import exit_program
from src.utils.tools import display_canvas_logo,sub_heading

def user_menu():
    print("\n" + "╔" + "═" * 78 + "╗")
    print(f"║{'USERS TERMINAL : [C A N V A S]':^78}║")
    print("╠" + "═" * 78 + "╣")
    options = [
        "Signup", 
        "Login", 
        "Exit"
        ]
    for i,opt in enumerate(options,1):
        print(f"║ {i}. {opt:74}║")
    
    print("╚" + "═" * 78 + "╝")

def user_dashobard():
    display_canvas_logo("C  A  N  V  A  S","THE ART OF DINING","─── Est. 2026 ───")
    print("◈◇◈◇"*20)

    while True:
        user_menu()
        valid = Validator()
        option = valid.validoption(1,3)
        if option == 1:
            Signup().staff()
        elif option == 2:
            Login().login()
        elif option == 3:
            exit_program("Exiting","Goodbye! Have a Great Day.")
            break
        else:
            print("PLease select option carefully(option > 0)!")


