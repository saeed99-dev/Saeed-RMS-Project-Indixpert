import json
import os

class Filemode:
    def create_file(self,route):
        if not os.path.exists(route):
            with open(route,"w") as file:
                return json.dump([],file)

    def load_data(self,route):
        try:
            if os.path.getsize(route)==0:
                return []
            with open(route,"r") as file:
                return json.load(file)
        except Exception as e:
            print(e)

    def save_data(self,data,route):
        try:
            with open(route,"w") as file:
               return json.dump(data,file,indent=4)
        except Exception as e:
            print(e)



# print(e)
# userlog=load_data()
# datalog={
#     "error": str(e),
#     "time":str(datetime.now()),
#     "function name":"load_data",