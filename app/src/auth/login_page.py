from src.filehandling.filemode import Filemode
from src.dashboard.staff import staff_menu
from src.dashboard.admin import admin_menu


class Login:
    def __init__(self):
        self.userdata = Filemode().load_data()

    def login(self):
        print("======= Login Portal =======")
        found = False
        while True:
            input_email = input("Enter Your Email: ").strip()
            input_password = input("Enter your Password: ").strip()

            

            for user in self.userdata:
                if user["email"] == input_email and user["password"] == input_password:
                    print("Login Successfull!")
                    if user["role"] == "Admin":
                        admin_menu()  # cuurently keeping menu option only later keep all functional menu
                    elif user["role"] == "Staff":
                        staff_menu()
                    found = True
            if found == False:
                print("User Not Found! Please enter correct email or Password")
                continue

            return input_email, input_password
