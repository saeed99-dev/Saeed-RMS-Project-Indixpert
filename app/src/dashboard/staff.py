from src.security.validation import Validator

def staff_menu():
    print("====== Welcome To RMS Staff Dashboard ======")
    print("1. View Menu")
    print("2. Take Order")
    print("3. My Order")
    print("4. Book Table")
    print("5. Cancel Order")
    print("6. View Invoice")
    print("7. View Profile")
    print("8. Logout")


def manage_staff_menu():
    try:
        valid=Validator()
        choice = valid.validoption()
        if choice == 1:
            print("View Menu")
        elif choice == 2:
            print("Take Order")
        elif choice == 3:
            print("My Order")
        elif choice== 4:
            print("Book Table")
        elif choice == 5:
            print("Cancel Order")
        elif choice == 6:
            print("View Invoice")
        elif choice == 7:
            print("View Profile")
        elif choice == 8:
            print("Logout")
        else:
            print("Invalid Choice!")
    except Exception as e:
        print(e) 
