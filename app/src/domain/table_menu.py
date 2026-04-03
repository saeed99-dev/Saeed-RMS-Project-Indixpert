from datetime import datetime,timedelta
from src.model.models import PathModel
from src.filehandling.filemode import Filemode 
from src.security.validation import Validator

class Table:
    def __init__(self,table_id,capacity):
        self.table_id=table_id
        self.capacity=capacity
        self.isoccupied=False
        self.current_booking=None
        self.booking_details={}
    
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

        self.available_slots = [
            "12:00 PM - 02:00 PM",
            "02:00 PM - 04:00 PM",
            "04:00 PM - 06:00 PM",
            "06:00 PM - 08:00 PM",
            "08:00 PM - 10:00 PM",
            "10:00 PM - 12:00 AM"
        ]

    def display_table_status(self):
        print("\n" + "╔" + "═" * 60 + "╗")
        print(f"║{'TABLE STATUS : [C A N V A S]':^60}║")
        print("╚" + "═" * 60 + "╝")

        for table in self.tables:
            if table.isoccupied:
                status="🔴 OCCUPIED"
                details=f"Guest: {table.current_booking} | Slot: {table.bookin_details.get('time_slot')}"
                date_info=f"Date: {table.bookin_details.get('booking_date')}"
            else:
                status="🟢 AVAILABLE"
                details="Ready for the Guest"
                date_info="N/A"

            print(f" ┌── Table {table.table_id:02} ──────────────────────────────┐")
            print(f" │ Status: {status:<15} Capacity: {table.capacity:<3} Date: {date_info:<15}  │")
            print(f" │ {details:<63}   │")
            print(f" └──────────────────────────────────────────┘")


    def book_table(self):
        try:
            name=input("Enter Guest Name: ").strip()
            if not name:
                print("Error: Guest name is compulsory.")
                return
            guest_count=int(input("Enter number of Guests: "))

            current_date_obj = datetime.now().date()
            max_future_date_obj = current_date_obj + timedelta(days=7)
            
            print(f"\nBooking available from: {current_date_obj.strftime('%d-%m-%Y')} to {max_future_date_obj.strftime('%d-%m-%Y')}")
            date_input = input("Enter Booking Date (DD-MM-YYYY) [Leave empty for today]: ").strip()
            
            if not date_input:
                booking_date_obj = current_date_obj
            else:
                try:
                    booking_date_obj = datetime.strptime(date_input, "%d-%m-%Y").date()
                except ValueError:
                    print("Error: Invalid date format. Please use DD-MM-YYYY.")
                    return
            if booking_date_obj < current_date_obj:
                print(f"Error: Cannot book for a past date ({booking_date_obj.strftime('%d-%m-%Y')}).")
                return
            if booking_date_obj > max_future_date_obj:
                print(f"Error: Bookings only allowed up to 7 days ahead (Max: {max_future_date_obj.strftime('%d-%m-%Y')}).")
                return

            booking_date_str = booking_date_obj.strftime("%d-%m-%Y")
            
            print("\nAvailable Time Slots:")
            for i, slot in enumerate(self.available_slots, 1):
                print(f"  {i}. {slot}")
            
            slot_choice_raw = input(f"Select Time Slot (1-{len(self.available_slots)}): ")
            if not slot_choice_raw.isdigit():
                print("Error: Please enter a valid number for the slot.")
                return
                
            slot_choice = int(slot_choice_raw)
            if 1 <= slot_choice <= len(self.available_slots):
                time_slot = self.available_slots[slot_choice - 1]
            else:
                print("Error: Invalid slot selection.")
                return

            assigned_table=None

            for table in self.tables:
                if not table.isoccupied and table.capacity>=guest_count:
                    assigned_table=table
                    break


            if assigned_table!=None:
                booking_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                assigned_table.isoccupied=True
                assigned_table.current_booking=name
                assigned_table.booking_details = {
                    "booking_date": booking_date_str,
                    "time_slot": time_slot
                }

                table_booked={
                    "name":name,
                    "guests":guest_count,
                    "table_id":assigned_table.table_id,
                    "book_time":booking_time,
                    "book_date":booking_date_str,
                    "time_slot":time_slot,
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
                        table.booking_details={}

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
            print(f"{'Date':<12} | {'Slot':<20} | {'Guest':<15} | {'T-ID':<5} | {'Count':<5} | {'Status'}")
            print("─"*90)
            for book in self.booking_history:
                print(f"{book['book_date']:<12} | {book['time_slot']:<20} | {book['name']:<15} | {book['table_id']:<5} | {book['guests']:<5} | {book['status']}")
            print("═"*90)

    def table_dashboard(self):

        while True:
            print("\n" + "╔" + "═" * 78 + "╗")
            print(f"║{'MANAGE TABLE : [C A N V A S]':^78}║")
            print("╠" + "═" * 78 + "╣")
            options = [
                "View Table Status", 
                "Book Table", 
                "Release Table (Checkout)", 
                "View History",  
                "Back"
                ]
            for i,opt in enumerate(options,1):
                print(f"║ {i}. {opt:76}║")
            
            print("╚" + "═" * 78 + "╝")

            choice=Validator().validoption(1,5)

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
