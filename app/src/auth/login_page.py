from src.filehandling.filemode import Filemode
from src.domain.staff_menu import staff_dashboard
from src.domain.admin_menu import admin_interface
from src.security.validation import Validator
from src.model.models import PathModel
from src.utils.tools import sub_heading


class Login:
    def __init__(self):
        self.userdata = Filemode().load_data(PathModel().user_data)

    def login(self):
        valid = Validator()
        sub_heading("LOGIN PORTAL : [C A N V A S]")
        found = False
        while True:
            input_email = valid.validemail()
            input_password = valid.validpassword()

            for user in self.userdata:
                if user["email"] == input_email and user["password"] == input_password:
                    if user["role"] != "Blocked":
                        if user["role"] == "Admin":
                            admin_interface()
                        elif user["role"] == "Staff":
                            staff_dashboard()
                        print("Login Successfull!")
                    else:
                        print("You are Blocked! Contact to Admin")
                    found = True
            if found == False:
                print("User Not Found! Please enter correct email or Password")
                continue

            return input_email, input_password
