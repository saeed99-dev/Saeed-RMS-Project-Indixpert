from pwinput import pwinput

class Validator:
    def __init__(self):
        pass

    def validname(self):
        while True:
            try:
                name = input("Enter your name: ").strip().title()

                if not name.isalpha():
                    print("Error: Name must include only alphabet.")
                    continue

                if len(name) < 4:
                    print("Error: Name must include at least 4 character")
                    continue

                repeat = False
                lower_name = name.lower()
                for i in range(len(name) - 2):
                    if lower_name[i] == lower_name[i + 1] == lower_name[i + 2]:
                        repeat = True
                        break

                if repeat:
                    print("Error: Name cannot contain more than 2 consecutive repetitive characters.")
                    continue
                else:
                    self.name = name
                    break
            except Exception as e:
                print(e)
        return name


    def validnumber(self):
        while True:
            try:
                number = input("Enter your number: ").strip()

                if not number.isdigit():
                    print("Error: Number must include only whole number.")

                elif number[0] == "0":
                    print("Error: First digit should not be Zero")

                elif len(number) != 10:
                    print("Error: Number must contain 10 digits")

                else:
                    self.number = number
                    break
            except Exception as e:
                print(e)
        return number


    def validemail(self):
        while True:
            try:
                email = input("Enter your Gmail: ").strip().lower()
                if not email:
                    print("Gmail can't be empty")

                elif "@" not in email:
                    print("Gmail must contain '@'.")
                elif "." not in email:
                    print("Gmail must contain '.'")
                elif not len(email) > 10:
                    print("Length of Gmail must not be less than 10")

                else:
                    self.email = email
                    break
            except Exception as e:
                print(e)
        return email


    def validpassword(self):
        while True:
            try:
                password = pwinput("Enter Your Password : ")

                if not len(password) > 5:
                    print("Error: Length of password must not be less than 6 character")
                    continue

                if len(password) == 0:
                    print("Password cannot be empty.")
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

                if not has_upper:
                    print("Password must include at least one uppercase letter.")
                    continue

                if not has_lower:
                    print("Password must include at least one lowercase letter.")
                    continue

                if not has_special:
                    print("Password must include at least one special character.")
                    continue

                if not has_digit:
                    print("Password must include at least one digit.")
                    continue

                repeate = False
                for i in range(len(password) - 2):
                    if password[i] == password[i + 1] == password[i + 2]:
                        repeate = True
                        continue

                if repeate:
                    print("Password cannot have more than 2 consecutive similar characters.")
                else:
                    self.password = password
                    break
            except Exception as e:
                print(e)
        return password

    def validoption(self):
        while True:
            
            option=input("Select Your Option: ")
            if not option:
                print("Input cannot be empty.\n")
                continue
            if option.isdigit():
                self.option=int(option)
                break
            else:
                print("It must be a positive integer only (no letters or symbols).")
        return int(option)


    def valid_id(self):
        pass




# Validname()
# Validnumber()
# Validemail()
# Validpassword()
# Validoption().choice()
# Valid_id()
