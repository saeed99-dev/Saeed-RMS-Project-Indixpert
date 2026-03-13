import uuid
from src.security.validation import Validator
from src.filehandling.filemode import Filemode


file=Filemode()
Filemode().create_file()
userdata=file.load_data()

valid=Validator()

class Signup:
    # def __init__(self):
    #     self.userdata=file.load_data()

    def admin(self):
        print("===== Admin Signup Portal =====")
 
        user={
            "name":valid.validname(),
            "email":valid.validemail(),
            "password":valid.validpassword(),
            "mobile":valid.validnumber(),
            "role":"Admin",
            "id":str(uuid.uuid4())[0:8]
        }

        userdata.append(user)
        file.save_data(userdata)    
        print("Signup Successfully!")



    def staff(self):
        print("===== Staff Signup Portal =====")
        
        user={
            "name":valid.validname(),
            "email":valid.validemail(),
            "password":valid.validpassword(),
            "mobile":valid.validnumber(),
            "role":"Staff",
            "id":str(uuid.uuid4())[0:8]
        }

        userdata.append(user)
        file.save_data(userdata)    
        print("Signup Successfully!")


# sign=Signup()