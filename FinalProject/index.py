def menu_function():
    print("Welcome to MONZO APP")
    print("Manage your finance with your finger tip.")
    print("1. Login (already have account?)")
    print("2. Register (create new account)")
def register():
    first_name = input("First name : ")
    last_name = input("Middle name and Last name: ")
    phone_number = input("firstname")
    email = input("firstname")
    address = input("location")
    dob = input("Date of birth: ")
    gender = input("Gender: ")
    data = {"first_name":first_name,"last_name":last_name,"phone_number":phone_number,"email":email,"address":address,"dob":dob,"gender":gender}

def add(user_type = 0):
    data = register()
    print(data)
    if user_type == 1:
        pass
    data["age"]= 10#calculate using date
    data["account_id"]
    data["account_number"]
    data["current_balance"]
    data["date_opened"] 
    data["status"]  # active / deactive/ closed
    if data["status"] == "closed":
        data["closed"]0
def convert_to_dict_(data):
    pass
def main_menu(username):
    print("<------ MONZO BANING MANAGEMENT SYSTEM (*_*) ------->")
    print("\tWelcome, ",str(username).upper())
    print("1. Make a transaction")
    print("2. Create new account")
    print("2. Read Details")
    print("3. Update Details")
    print("3. Remove Account.")
    print("4. Search Transaction")
def login(username,password):
    if username == "rahul" and password == 'rahul316':
        main_menu()


def register():
    ...
def main():
    """
    Main application entry point with an improved menu system.
    Continues until user chooses to exit.
    """
    while True:
        print("\nMenu Options:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        try:
            option = input("Please select an option (1-3): ")
            
            if option == '1':
                login()
            elif option == '2':
                register()
            elif option == '3':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid option. Please select 1, 2, or 3.")
        except ValueError as e:
            print(f"Input error: {e}")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
