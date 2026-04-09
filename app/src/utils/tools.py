from datetime import datetime
from src.filehandling.filemode import Filemode
from src.model.models import PathModel
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def exit_program(operation,massage):
    try:
        print(f"{Fore.GREEN}{operation}", end="", flush=True)
        for _ in range(5):
            time.sleep(0.25)
            print(f"{Fore.GREEN}.", end="", flush=True)

        print(f"\n{Fore.YELLOW}{massage}{Style.RESET_ALL}")
    except Exception as e:
        exit_data={
            "error": str(e),
            "time": str(datetime.now()),
            "function name": "exit_program",
        }
        Filemode().append_data(exit_data,PathModel().security_log)
        print(f"\n{operation}...\n{massage}")
    

def display_canvas_logo(title, subtitle, date):
    print("\n" + Fore.CYAN + "╔" + "═" * 78 + "╗")
    print(f"{Fore.CYAN}{'║':<78} {'║'}")
    print(f"{Fore.CYAN}{'║':<31}{Fore.WHITE}{title}{Fore.CYAN}{'║':>31}")
    print(f"{Fore.CYAN}{'║':<31}{Fore.WHITE}{subtitle}{Fore.CYAN}{'║':>31}")
    print(f"{Fore.CYAN}║{Fore.WHITE}{date:^78}{Fore.CYAN}║")
    print(f"{Fore.CYAN}{'║':<78} {'║'}")
    print(Fore.CYAN + "╚" + "═" * 78 + "╝")



def main_subheading(text):
    canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
    full_text = f"{text} :  {canvas_fore}"

    print("\n" + Fore.CYAN + "╔" + "═" * 78 + "╗")
    print(f"{Fore.CYAN}║{Fore.YELLOW}{full_text:>94}{Fore.CYAN}{'║':>24}")
    print(Fore.CYAN +"╚" + "═" * 78 + "╝")

def staff_subheading(text):
    canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
    full_text = f"{text} :  {canvas_fore}"

    print("\n" + Fore.BLUE + "╔" + "═" * 78 + "╗")
    print(f"{Fore.BLUE}║{Fore.YELLOW}{full_text:>94}{Fore.BLUE}{'║':>24}")
    print(Fore.BLUE +"╚" + "═" * 78 + "╝")

def admin_subheading(text):
    canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
    full_text = f"{text} :  {canvas_fore}"

    print("\n" + Fore.GREEN + "╔" + "═" * 78 + "╗")
    print(f"{Fore.GREEN}║{Fore.YELLOW}{full_text:>94}{Fore.GREEN}{'║':>24}")
    print(Fore.GREEN +"╚" + "═" * 78 + "╝")

def connect_subheading(text):
    canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
    full_text = f"{text} :  {canvas_fore}"

    print("\n" + Fore.BLUE + "╔" + "═" * 78 + "╗")
    print(f"{Fore.BLUE}║{Fore.YELLOW}{full_text:>94}{Fore.BLUE}{'║':>24}")
    print(Fore.BLUE +"╠" + "═" * 78 + "╣")

def press_to_continue(press_button,return_page):
    input(f"\n Press [{press_button}] to return to the {return_page} ")

# display_canvas_logo("C A N V A S","THE ART OF DINING", "Est. 2026")
# exit_program("Exiting","GoodBye!")
# press_to_continue("Enter","Dashboard")
# canvas()