from src.filehandling.filemode import Filemode
from src.model.models import PathModel

class User:
    def __init__(self):
        self.users=Filemode().load_data(PathModel().user_data)
    
    def view_staff_profile(self):
        print("\nSTAFF PROFILE DIRECTORY : [C A N V A S]")
        print("-" * 60)
        print(f"{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}")
        print("-" * 60)

        staff_found=False
        for user in self.users:
            if user["role"]=="Staff":
                print(f"{user['id']:<10} | {user['name']:<10} | {user['role']:<8} | {user['email']:<20} | {user['mobile']:<10}")
                print("-" * 60)
                staff_found=True
        
        if not staff_found:
            print(f"{'No Staff Member Found':^60}")
            print("-" * 60)

        print("=" * 60)

    def view_admin_profile(self):
        print("\nADMIN PROFILE DIRECTORY : [C A N V A S]")
        print("-" * 60)
        print(f"{'ID':<10} | {'Name':<10} | {'Role':<8} | {'Email':<20} | {'Mobile':<10}")
        print("-" * 60)

        admin_found=False
        for user in self.users:
            if user["role"]=="Admin":
                print(f"{user['id']:<10} | {user['name']:<10} | {user['role']:<8} | {user['email']:<20} | {user['mobile']:<10}")
                print("-" * 60)
                admin_found=True
        
        if not admin_found:
            print(f"{'No Admin Member Found':^60}")
            print("-" * 60)

        print("=" * 60)
    
    
