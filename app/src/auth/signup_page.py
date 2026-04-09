import uuid
from src.security.validation import Validator
from src.filehandling.filemode import Filemode
from src.model.models import PathModel
from src.utils.tools import main_subheading
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Signup:
   
    def staff(self):
        try:
            file=Filemode()
            Filemode().create_file(PathModel().user_data)
            userdata=file.load_data(PathModel().user_data)

            valid=Validator()
            main_subheading("SIGNUP PORTAL")

            while True:
                try:
                    email=valid.validemail()
                    email_exists=False
                    
                    for data in userdata:
                        if data.get('email')==email:
                            email_exists=True
                            break

                    if email_exists:
                        print(f"{Fore.RED}Error: This email {Fore.WHITE}{email} {Fore.RED}is already registered.")
                    else:
                        break
                except Exception as e:
                    print(f"{Fore.RED}Input error during email validation: {e}")
                    continue
            
            user={
                "name":valid.validname(),
                "email":email,
                "password":valid.validpassword(),
                "mobile":valid.validnumber(),
                "role":"Staff",
                "id":str(uuid.uuid4())[0:8]
            }

            userdata.append(user)
            file.save_data(userdata,PathModel().user_data)    
            print(f"\n{Fore.GREEN}Signup Successful! Welcome to the team, {Fore.WHITE}{user['name']}.")
            print(f"{Fore.CYAN}Your Staff ID is: {Fore.WHITE}{user['id']}")
    
        except Exception as e:
            signup_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "user_menu",
            }
            Filemode().append_data(signup_data,PathModel().athu_log)
            print(f"{Fore.RED}An unexpected error occurred during signup: {e}")


# sign=Signup()