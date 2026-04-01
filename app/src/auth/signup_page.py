import uuid
from src.security.validation import Validator
from src.filehandling.filemode import Filemode
from src.model.models import PathModel
from src.utils.tools import sub_heading

class Signup:
   
    def staff(self):
        file=Filemode()
        Filemode().create_file(PathModel().user_data)
        userdata=file.load_data(PathModel().user_data)

        valid=Validator()

        sub_heading("SIGNUP PORTAL : [C A N V A S]")

        while True:
            email=valid.validemail()
            email_exists=False
            for data in userdata:
                if data.get('email')==email:
                    email_exists=True
                    break
            if email_exists:
                print(f"Error: This email {email} is already registered.")
            else:
                break
        
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
        print("Signup Successfully!")


# sign=Signup()