import time

def exit_program(operation,massage):
    print(operation, end="")
    for _ in range(5):
        time.sleep(0.25)
        print(".", end="")
    print(f"\n{massage}")
    

def display_canvas_logo(title,subtitle,date):
    width = 60
    print("╔" + "═" * (width - 2) + "╗")
    print("║" + " " * (width - 2) + "║")
    print("║" + title.center(width - 2) + "║")
    print("║" + subtitle.center(width - 2) + "║")
    print("║" + date.center(width - 2) + "║")
    print("║" + " " * (width - 2) + "║")
    print("╚" + "═" * (width - 2) + "╝")

def sub_heading(text):
    width=60
    print("╔" + "═" * (width - 2) + "╗")
    print("║" + text.center(width - 2) + "║")
    print("╚" + "═" * (width - 2) + "╝")



def press_to_continue(press_button,return_page):
    input(f"\n Press [{press_button}] to return to the {return_page} ")

# display_canvas_logo("C A N V A S","THE ART OF DINING", "Est. 2026")
# exit_program("Exiting","GoodBye!")
# press_to_continue("Enter","Dashboard")