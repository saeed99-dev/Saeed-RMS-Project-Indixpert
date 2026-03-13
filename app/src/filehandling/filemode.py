import json
import os

class Filemode:
    def __init__(self):
        self.route=r"C:\Indixpert_Saeed\GitHub-nov25-C\Saeed-RMS-Project-Indixpert\app\src\database\user.json"
        
    def create_file(self):
        if not os.path.exists(self.route):
            with open(self.route,"w") as file:
                return json.dump([],file)

    def load_data(self):
        try:
            if os.path.getsize(self.route)==0:
                return []
            with open(self.route,"r") as file:
                return json.load(file)
        except Exception as e:
            print(e)

    def save_data(self,data):
        try:
            with open(self.route,"w") as file:
               return json.dump(data,file,indent=4)
        except Exception as e:
            print(e)



# print(e)
# userlog=load_data()
# datalog={
#     "error": str(e),
#     "time":str(datetime.now()),
#     "function name":"load_data",