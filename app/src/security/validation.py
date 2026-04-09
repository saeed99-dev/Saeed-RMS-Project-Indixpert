from pwinput import pwinput
from datetime import datetime
from src.filehandling.filemode import Filemode
from src.model.models import PathModel
import colorama
from colorama import Fore,Style

colorama.init(autoreset=True)


class Validator:
    def __init__(self):
        self.name = None
        self.number = None
        self.email = None
        self.password = None
        self.option = None

    def validname(self):
        while True:
            try:
                name = input(f"{Fore.CYAN}Enter your name: {Style.RESET_ALL}").strip().title()

                if not name.isalpha():
                    print(f"{Fore.RED}Error: Name must include only alphabet.")
                    continue

                if len(name) < 4:
                    print(f"{Fore.RED}Error: Name must include at least 4 character")
                    continue

                repeat = False
                lower_name = name.lower()
                for i in range(len(name) - 2):
                    if lower_name[i] == lower_name[i + 1] == lower_name[i + 2]:
                        repeat = True
                        break

                if repeat:
                    print(f"{Fore.RED}Error: Name cannot contain more than 2 consecutive repetitive characters.")
                    continue
                else:
                    self.name = name
                    return name
            except Exception as e:
                name_validation_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "validname",
                }
                Filemode().append_data(name_validation_data,PathModel().security_log)
                print(f"{Fore.YELLOW}An unexpected error occurred: {e}")
        


    def validnumber(self):
        while True:
            try:
                number = input(f"{Fore.CYAN}Enter your number: {Style.RESET_ALL}").strip()

                if not number.isdigit():
                    print(f"{Fore.RED}Error: Number must include only whole number.")

                elif number[0] == "0":
                    print(f"{Fore.RED}Error: First digit should not be Zero")

                elif len(number) != 10:
                    print(f"{Fore.RED}Error: Number must contain 10 digits")

                else:
                    self.number = number
                    return number
            except Exception as e:
                number_validation_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "validnumber",
                }
                Filemode().append_data(number_validation_data,PathModel().security_log)
                print(f"{Fore.YELLOW}An unexpected error occurred: {e}")
        


    def validemail(self):
        while True:
            try:
                email = input(f"{Fore.CYAN}Enter your Gmail: {Style.RESET_ALL}").strip().lower()
                if not email:
                    print(f"{Fore.RED}Error: Gmail can't be empty")
                    continue
                at_count = email.count("@")
                dot_count = email.count(".")

                if at_count != 1:
                    print(f"{Fore.RED}Invalid: Gmail must contain exactly one '@'.")
                elif dot_count != 1:
                    print(f"{Fore.RED}Invalid: Gmail must contain exactly one '.'.")
                elif email.find(".") < email.find("@"):
                    print(f"{Fore.RED}Invalid: The '.' must come after the '@' symbol.")
                elif len(email) < 10:
                    print(f"{Fore.RED}Length of Gmail must not be less than 10 characters.")
                elif email.startswith("@") or email.endswith("."):
                    print(f"{Fore.RED}Invalid email format (cannot start with @ or end with .).")
                else:
                    self.email = email
                    return email
                    
            except Exception as e:
                email_validation_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "validmail",
                }
                Filemode().append_data(email_validation_data,PathModel().security_log)
                print(f"{Fore.YELLOW}An unexpected error occurred: {e}")


    def validpassword(self):
        while True:
            try:
                password = pwinput(prompt=f"{Fore.CYAN}Enter Your Password: {Style.RESET_ALL}", mask="*")

                if len(password) < 6:
                    print(f"{Fore.RED}Error: Length of password must not be less than 6 character")
                    continue

                has_upper = False
                has_lower = False
                has_special = False
                has_digit = False

                for char in password:
                    if char.isupper():
                        has_upper = True
                    elif char.islower():
                        has_lower = True
                    elif not char.isalnum():
                        has_special = True
                    elif char.isdigit():
                        has_digit = True

                if not (has_upper and has_lower and has_special and has_digit):
                    print(f"{Fore.RED}Error: Password must include uppercase, lowercase, digit, and special character.")
                    continue

                repeate = False
                for i in range(len(password) - 2):
                    if password[i] == password[i + 1] == password[i + 2]:
                        repeate = True
                        break

                if repeate:
                    print(f"{Fore.RED}Error: Password cannot have more than 2 consecutive similar characters.")
                else:
                    self.password = password
                    return password
            except Exception as e:
                password_validation_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "validpassword",
                }
                Filemode().append_data(password_validation_data,PathModel().security_log)
                print(f"{Fore.YELLOW}An unexpected error occurred: {e}")

    def validoption(self,min,max):
        while True:
            try:
                option=input(f"{Fore.GREEN}Select Your Option ({min}-{max}): {Style.RESET_ALL}")
                if not option:
                    print(f"{Fore.RED}Input cannot be empty.\n")
                    continue

                if option.isdigit():
                    val=int(option)
                    if min<=val <=max:
                        self.option = val
                        return val
                    else:
                        print(f"{Fore.RED}Error: Choice must be between {min} and {max}.\n")
                    break
                else:
                    print(f"{Fore.RED}Error: It must be a positive integer only (no letters or symbols).")
            except Exception as e:
                option_validation_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "validoption",
                }
                Filemode().append_data(option_validation_data,PathModel().security_log)
                print(f"{Fore.YELLOW}An unexpected error occurred: {e}")





# Validname()
# Validnumber()
# Validemail()
# Validpassword()
# Validoption().choice()
# Valid_id()

# Validator().validoption(1,3)
