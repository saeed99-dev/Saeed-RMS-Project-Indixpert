from datetime import datetime,timedelta
from src.model.models import PathModel
from src.filehandling.filemode import Filemode 
from src.security.validation import Validator
from src.utils.tools import connect_subheading,admin_subheading
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

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
        try:
            canvas_fore = f"{Fore.WHITE}[ {Fore.RED}C{Fore.GREEN} A{Fore.YELLOW} N{Fore.BLUE} V{Fore.MAGENTA} A{Fore.CYAN} S {Style.RESET_ALL}]"
            full_text = f"TABLE STATUS :  {canvas_fore}"
            print("\n" + Fore.BLUE + "╔" + "═" * 60 + "╗")
            print(f"{Fore.BLUE}{'║':<15}{Fore.YELLOW}{full_text}{Fore.BLUE}{'║':>16}")
            print(Fore.BLUE + "╚" + "═" * 60 + "╝")
            # staff_subheading("TABLE STATUS")

            for table in self.tables:
                if table.isoccupied:
                    status=f"{Fore.RED}🔴 OCCUPIED"
                    details=f"Guest: {Fore.WHITE}{table.current_booking} {Fore.CYAN}| Slot: {Fore.WHITE}{table.booking_details.get('time_slot')}"
                    date_info=f"Date: {Fore.WHITE}{table.booking_details.get('booking_date')}"
                else:
                    status=f"{Fore.GREEN}🟢 AVAILABLE"
                    details=f"{Fore.WHITE}Ready for the Guest"
                    date_info=f"{Fore.WHITE}N/A"

                print(f"{Fore.BLUE} ┌── Table {table.table_id:02} ──────────────────────────────┐")
                print(f"{Fore.BLUE} │ {Fore.CYAN}Status: {status:<15} {Fore.CYAN}Capacity: {Fore.WHITE}{table.capacity:<3} {Fore.CYAN}Date: {date_info:<15}")
                print(f"{Fore.BLUE} │ {details:<43}   {Fore.BLUE}│")
                print(f"{Fore.BLUE} └──────────────────────────────────────────┘")
        except Exception as e:
            display_table_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "display_table_status",
            }
            Filemode().append_data(display_table_data,PathModel().table_log)
            print(f"{Fore.RED}Error displaying table status: {e}")

    def book_table(self):
        try:
            admin_subheading("BOOK A TABLE")
            name=input(f"{Fore.CYAN}Enter Guest Name: {Style.RESET_ALL}").strip()
            if not name:
                print(f"{Fore.RED}Error: Guest name is compulsory.")
                return
            
            guest_count_raw=input(f"{Fore.CYAN}Enter number of Guests: {Style.RESET_ALL}")
            if not guest_count_raw.isdigit():
                print(f"{Fore.RED}Error: Please enter a valid number for guests.")
                return
            guest_count = int(guest_count_raw)

            current_date_obj = datetime.now().date()
            max_future_date_obj = current_date_obj + timedelta(days=7)
            
            print(f"\n{Fore.WHITE}Booking available from: {Fore.GREEN}{current_date_obj.strftime('%d-%m-%Y')} {Fore.WHITE}to {Fore.GREEN}{max_future_date_obj.strftime('%d-%m-%Y')}")
            date_input = input(f"{Fore.CYAN}Enter Booking Date (DD-MM-YYYY) [Leave empty for today]: {Style.RESET_ALL}").strip()
            
            if not date_input:
                booking_date_obj = current_date_obj
            else:
                try:
                    booking_date_obj = datetime.strptime(date_input, "%d-%m-%Y").date()
                except ValueError:
                    date_input_data={
                        "error": str(e),
                        "time": str(datetime.now()),
                        "function name": "date_input",
                    }
                    Filemode().append_data(date_input_data,PathModel().table_log)
                    print(f"{Fore.RED}Error: Invalid date format. Please use DD-MM-YYYY.")
                    return
            if booking_date_obj < current_date_obj:
                print(f"{Fore.RED}Error: Cannot book for a past date ({booking_date_obj.strftime('%d-%m-%Y')}).")
                return
            if booking_date_obj > max_future_date_obj:
                print(f"{Fore.RED}Error: Bookings only allowed up to 7 days ahead (Max: {max_future_date_obj.strftime('%d-%m-%Y')}).")
                return

            booking_date_str = booking_date_obj.strftime("%d-%m-%Y")
            
            print(f"\n{Fore.YELLOW}Available Time Slots:")
            for i, slot in enumerate(self.available_slots, 1):
                print(f"  {Fore.CYAN}{i}. {Fore.WHITE}{slot}")
            
            slot_choice_raw = input(f"{Fore.CYAN}Select Time Slot (1-{len(self.available_slots)}): {Style.RESET_ALL}")
            if not slot_choice_raw.isdigit():
                print(f"{Fore.RED}Error: Please enter a valid number for the slot.")
                return
                
            slot_choice = int(slot_choice_raw)
            if 1 <= slot_choice <= len(self.available_slots):
                time_slot = self.available_slots[slot_choice - 1]
            else:
                print(f"{Fore.RED}Error: Invalid slot selection.")
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

                print(f"\n {Fore.GREEN}SUCCESS! Mr/Mrs {name} Total-{guest_count} seats is assigend to Table- 0{assigned_table.table_id}")
            else:
                print(f"{Fore.RED}Sorry,Table is not available for {guest_count} number of seats. ")
        except Exception as e:
            table_booking_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "book_table",
            }
            Filemode().append_data(table_booking_data,PathModel().table_log)
            print(f"{Fore.RED}Critical Booking Error: {e}")
    
    def release_table(self):
        try:
            admin_subheading("RELEASE / CHECKOUT TABLE")
            # sub_heading(f"{Fore.YELLOW}RELEASE / CHECKOUT TABLE")
            table_id_raw=input(f"{Fore.CYAN}Enter Table ID to checkout: {Style.RESET_ALL}").strip()

            if not table_id_raw.isdigit():
                print(f"{Fore.RED}Error: Table ID must be a numeric value.")
                return
            
            table_id = int(table_id_raw)
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
                        print(f"\n{Fore.GREEN}SUCCESS: Table {table_id:02} is now free and ready for new guests.")
                    else:
                        print(f"{Fore.YELLOW}Notice: Table {table_id:02} is already empty.")
                        break
            
            if not found:
                print(f"{Fore.RED}Error: Table ID {table_id} does not exist in the system.")
        except Exception as e:
            table_releasing_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "release_table",
            }
            Filemode().append_data(table_releasing_data,PathModel().table_log)
            print(f"{Fore.RED}An error occurred during checkout: {e}")

    def view_history(self):
        try:
            admin_subheading("TABLE BOOKING HISTORY")

            if not self.booking_history:
                print(f"{Fore.YELLOW}No Booking Recorded Yet.")
            else:
                print(f"{Fore.CYAN}{'Date':<12} | {'Slot':<20} | {'Guest':<10} | {'T-ID':<5} | {'Count':<5} | {'Status'}")
                print(Fore.BLUE + "─"*80)

                for book in self.booking_history:
                    status_color = Fore.GREEN if book['status'] == "Active" else Fore.WHITE
                    
                    print(f"{Fore.WHITE}{book['book_date']:<12} | "
                          f"{book['time_slot']:<20} | "
                          f"{book['name'].capitalize():<10} | "
                          f"{book['table_id']:<5} | "
                          f"{book['guests']:<5} | "
                          f"{status_color}{book['status']}")
                print(Fore.CYAN + "═"*80)
        except Exception as e:
            booking_history_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "view_history",
            }
            Filemode().append_data(booking_history_data,PathModel().table_log)
            print(f"{Fore.RED}Error viewing history: {e}")


    def table_dashboard(self):

        while True:
            try:
                connect_subheading("MANAGE TABLE")
                options = [
                    "View Table Status", 
                    "Book Table", 
                    "Release Table (Checkout)", 
                    "View History",  
                    "Back"
                    ]
                for i,opt in enumerate(options,1):
                    print(f"{Fore.BLUE}║ {Fore.YELLOW}{i}. {Fore.WHITE}{opt:74}{Fore.BLUE}║")
                
                print(Fore.BLUE + "╚" + "═" * 78 + "╝")

                choice=Validator().validoption(1,5)

                if choice==1:
                    self.display_table_status()
                    input(f"{Fore.YELLOW}Press [Enter] to Go Back {Style.RESET_ALL}")
                elif choice==2:
                    self.book_table()
                elif choice==3:
                    self.release_table()
                elif choice==4:
                    self.view_history()
                    input(f"\n{Fore.YELLOW}Press [Enter] to Show the Dashboard {Style.RESET_ALL}")
                elif choice==5:
                    print(f"{Fore.WHITE}Returning to main menu...")
                    break
                else:
                    print(f"{Fore.RED}Invalid Option! Please select between 1-5.")
            except Exception as e:
                table_dashboard_data={
                "error": str(e),
                "time": str(datetime.now()),
                "function name": "table_dashboard",
                }
                Filemode().append_data(table_dashboard_data,PathModel().table_log)
                print(f"{Fore.RED}Dashboard Error: {e}")
                break


# TableManager().table_dashboard()





# manager=TableManager()
# manager.display_table_status()
# manager.book_table()
# manager.display_table_status()
# manager.release_table()
