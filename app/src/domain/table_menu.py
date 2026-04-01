from datetime import datetime
from src.model.models import PathModel
from src.filehandling.filemode import Filemode 

class Table:
    def __init__(self,table_id,capacity):
        self.table_id=table_id
        self.capacity=capacity
        self.isoccupied=False
        self.current_booking=None
    
class TableManager:
    def __init__(self):
        self.table_data=Filemode().load_data(PathModel().table_data)
        self.tables=[
            Table(1,2), 
            Table(2,2),
            Table(3,4), 
            Table(4,4),
            Table(5,6), 
            Table(6,8)
        ]
        self.booking_history=[]

    def display_table_status(self):
        print("\n" + "╔" + "═" * 50 + "╗")
        print(f"║{'TABLE STATUS : [C A N V A S]':^50}║")
        print("╚" + "═" * 50 + "╝")

        for table in self.tables:
            if table.isoccupied:
                status="🔴 OCCUPIED"
            else:
                status="🟢 AVAILABLE"

            if table.isoccupied:
                customer=f"Guest: {table.current_booking}"
            else:
                customer="Ready for the Guest"

            print(f" ┌── Table {table.table_id:02} ──────────────────────────────┐")
            print(f" │ Status: {status:<15} Capacity: {table.capacity:<3}   │")
            print(f" │ {customer:<38}   │")
            print(f" └──────────────────────────────────────────┘")


    def book_table(self):
        try:
            name=input("Enter Guest Name: ").strip()
            if not name:
                print("Error: Guest name is compulsory.")
                return
            guest_count=int(input("Enter number of Guests: "))

            assigned_table=None

            for table in self.tables:
                if not table.isoccupied and table.capacity>=guest_count:
                    assigned_table=table
                    break


            if assigned_table!=None:
                booked_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                assigned_table.isoccupied=True
                assigned_table.current_booking=name

                table_booked={
                    "name":name,
                    "guests":guest_count,
                    "table_id":assigned_table.table_id,
                    "time":booked_time,
                    "status":"Active"
                }
                self.booking_history.append(table_booked)
                Filemode().save_data(self.booking_history,PathModel().table_data)

                print(f"\n SUCCESS! Mr/Mrs {name} Total-{guest_count} seats is assigend to Table- 0{assigned_table.table_id}")
            else:
                print(f"Sorry,Table is not available for {guest_count} number of seats. ")
        except Exception as e:
            print(e)
    
    def release_table(self):
        try:
            table_id=int(input("Enter Table ID to checkout: "))

            found=False
            for table in self.tables:
                if table.table_id==table_id:
                    found=True
                    if table.isoccupied:
                        for book in self.booking_history:
                            if book["table_id"]==table_id and book["status"]=="Active":
                                book["status"]="Complete"

                        table.isoccupied=False
                        table.current_booking=None

                        Filemode().save_data(self.booking_history,PathModel().table_data)
                        print(f"Table {table_id} is now free")
                        
                    else:
                        print("Table is already Empty")
                        return
            
            if not found:
                print("Table ID not found.")
        except Exception as e:
            print(e)

    def view_history(self):
        print("\n" + "═"*52)
        print(f"{'TABLE BOOKING HISTORY : [C A N V A S]':^52}")
        print("═"*52)

        if not self.booking_history:
            print("No Booking Recorded Yet.")
        else:
            print(f"{'Time':<20}|{'Guest':<15}|{'Table':<5}|{'Guest'}")
            print("═"*52)
            for book in self.booking_history:
                print(f"{book['time']:<20}|{book['name']:<15}|{book['table_id']:<5}|{book['guests']}")
                print("═"*52)

    def table_dashboard(self):

        while True:
            print("\n" + "╔" + "═" * 58 + "╗")
            print(f"║{'MANAGE TABLE : [C A N V A S]':^58}║")
            print("╠" + "═" * 58 + "╣")
            options = [
                "View Table Status", 
                "Book Table", 
                "Release Table (Checkout)", 
                "View History",  
                "Back"
                ]
            for i,opt in enumerate(options,1):
                print(f"║ {i}. {opt:56}║")
            
            print("╚" + "═" * 58 + "╝")

            choice=int(input("\n Select Option(1-5): "))

            if choice==1:
                self.display_table_status()
                input("Press [Enter] to Go Back ")
            elif choice==2:
                self.book_table()
            elif choice==3:
                self.release_table()
            elif choice==4:
                self.view_history()
                input("Press [Enter] to Show the Dashboard ")
            elif choice==5:
                break
            else:
                print("Invalid Option!")


# TableManager().table_dashboard()





# manager=TableManager()
# manager.display_table_status()
# manager.book_table()
# manager.display_table_status()
# manager.release_table()
