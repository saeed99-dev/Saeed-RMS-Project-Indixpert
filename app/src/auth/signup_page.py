import uuid
from src.security.validation import Validator
from src.filehandling.filemode import Filemode

class Signup:
    
    def staff(self):
        file=Filemode()
        Filemode().create_file()
        userdata=file.load_data()

        valid=Validator()

        print("===== Signup Portal =====")

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
        file.save_data(userdata)    
        print("Signup Successfully!")


# sign=Signup()