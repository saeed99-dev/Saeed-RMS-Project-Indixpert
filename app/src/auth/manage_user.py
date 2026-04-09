from src.auth.signup_page import Signup
from src.auth.login_page import Login
from src.security.validation import Validator
from src.utils.tools import exit_program
from src.utils.tools import display_canvas_logo
from datetime import datetime
from src.filehandling.filemode import Filemode
from src.model.models import PathModel
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def user_menu():
    try:
        canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
        full_text = f"USERS TERMINAL :  {canvas_fore}"

        print("\n" + Fore.CYAN + "╔" + "═" * 78 + "╗")
        print(f"{Fore.CYAN}║{Fore.YELLOW}{full_text:>94}{Fore.CYAN}{'║':>24}")
        print(Fore.CYAN +"╠" + "═" * 78 + "╣")
        
        options = [
            "Signup", 
            "Login", 
            "Exit"
            ]
        for i,opt in enumerate(options,1):
            print(f"{Fore.CYAN}║ {Fore.YELLOW}{i}. {Fore.WHITE}{opt:74}{Fore.CYAN}║")
        
        print(Fore.CYAN + "╚" + "═" * 78 + "╝")
    except Exception as e:
        user_menu_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "user_menu",
            }
        Filemode().append_data(user_menu_data,PathModel().athu_log)
        print(f"{Fore.RED}Error rendering menu: {e}")

def user_dashobard():
    canvas_back=f"{Back.RED} C {Back.GREEN} A {Back.YELLOW} N {Back.BLUE} V {Back.MAGENTA} A {Back.CYAN} S {Back.WHITE}"

    title_back = f"{Back.RED} C {Back.GREEN} A {Back.YELLOW} N {Back.BLUE} V {Back.MAGENTA} A {Back.CYAN} S {Style.RESET_ALL}"
    subtitle=f"{Fore.YELLOW}THE ART OF DINNING"

    try:
        display_canvas_logo(title_back,subtitle,"─── Est. 2026 ───")
        print(f"{Fore.CYAN}◈{Fore.YELLOW}◇"*40)

        while True:
            user_menu()
            try:
                valid = Validator()
                option = valid.validoption(1,3)
                if option == 1:
                    Signup().staff()
                elif option == 2:
                    Login().login()
                elif option == 3:
                    exit_program(f"{Fore.GREEN}Exiting","Goodbye! Have a Great Day.")
                    break
                else:
                    print(f"{Fore.RED}PLease select option carefully (option 1-3)!")
            except Exception as e:
                print(f"{Fore.RED}An error occurred during navigation: {e}")
    except Exception as e:
        user_dashobard_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "user_dashboard",
            }
        Filemode().append_data(user_dashobard_data,PathModel().athu_log)
        print(f"{Fore.RED}Fatal Dashboard Error: {e}")

