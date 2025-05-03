import datetime

# Sample data for initialization
sample_data = '''admin;1|john|doe|john.doe@email.com|admin1|pass123|1
admin;2|alice|smith|alice.smith@email.com|admin2|alicepwd|1
admin;3|bob|johnson|bob.j@email.com|admin3|bobpass|1
admin;4|maria|garcia|maria.g@email.com|admin4|mariapw|1
admin;5|david|lee|david.lee@email.com|admin5|davidpw|1
customer;1001|jane|smith|1990-01-01|jane.smith@email.com|janes1|pass1234|12345678|savings|500.00|1
customer;1002|tom|brown|1985-05-12|tom.brown@email.com|tomb2|tom12345|23456789|current|200.00|1
customer;1003|sara|davis|1992-07-23|sara.davis@email.com|sarad3|sara1234|34567890|savings|1000.00|1
customer;1004|mike|wilson|1988-11-30|mike.w@email.com|mikew4|mike1234|45678901|current|0.00|1
customer;1005|linda|martinez|1995-03-15|linda.m@email.com|lindam5|linda123|56789012|savings|100.00|1
transaction;5001|12345678|deposit|2025-04-23|100.00|600.00
transaction;5002|12345678|withdrawal|2025-04-23|200.00|400.00
transaction;5003|23456789|deposit|2025-04-22|300.00|500.00
transaction;5004|34567890|withdrawal|2025-04-21|400.00|600.00
transaction;5005|45678901|deposit|2025-04-20|100.00|100.00
transaction;5006|56789012|deposit|2025-04-19|1000.00|1100.00
transaction;5007|45678901|withdraw|2025-04-20|200.00|-100.00
'''

# Initialize db.txt if empty or not present
try:
    with open("db.txt", "r") as r:
        if r.read() == '':
            with open("db.txt", "w") as w:
                w.write(sample_data)
except FileNotFoundError:
    with open("db.txt", "w") as f:
        f.write(sample_data)

account_types = ["Savings Account", "Current Account"]

def post_API(sample_db, filename="db.txt"):
    with open(filename, 'w') as f:
        # Write admins
        for admin_id, admin in sample_db['admins'].items():
            line = (
                f"admin;{admin_id}|{admin['first_name']}|{admin['last_name']}|"
                f"{admin['email']}|{admin['username']}|{admin['password']}|{int(admin['is_superuser'])}\n"
            )
            f.write(line)
        # Write customers
        for customer_id, customer in sample_db['customers'].items():
            line = (
                f"customer;{customer_id}|{customer['first_name']}|{customer['last_name']}|{customer['dob']}|"
                f"{customer['email']}|{customer['username']}|{customer['password']}|{customer['account_number']}|"
                f"{customer['account_type']}|{customer['balance']:.2f}|{int(customer['is_active'])}\n"
            )
            f.write(line)
        # Write transactions
        for trans_id, trans in sample_db['transactions'].items():
            line = (
                f"transaction;{trans_id}|{trans['account_number']}|{trans['transaction_type']}|"
                f"{trans['date']}|{trans['amount']:.2f}|{trans['balance_after']:.2f}\n"
            )
            f.write(line)
    return get_API()

def get_data(data_type='c'):
    admin_list = []
    customer_list = []
    transaction_list = []
    with open('db.txt','r') as db:
        all_data = db.readlines()
    for line_data in all_data:
        db_type = line_data.split(';')[0]
        data = line_data.split(';')[1].split("|")
        if db_type == 'admin':
            admin_list.append(data)
        elif db_type == 'customer':
            customer_list.append(data)
        else:
            transaction_list.append(data)
    if data_type == 'a':
        return admin_list
    elif data_type == 'c':
        return customer_list
    else:
        return transaction_list

def get_API(filename='db.txt'):
    sample_db = {
        "admins": {},
        "customers": {},
        "transactions": {}
    }
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(';')
                record_type = parts[0]
                data = parts[1].split('|')
                if record_type == 'admin':
                    try:
                        admin_id = int(data[0])
                        sample_db["admins"][admin_id] = {
                            "first_name": data[1],
                            "last_name": data[2],
                            "email": data[3],
                            "username": data[4],
                            "password": data[5],
                            "is_superuser": bool(int(data[6]))
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Error parsing admin record: {data} ({e})")
                elif record_type == 'customer':
                    try:
                        customer_id = int(data[0])
                        sample_db["customers"][customer_id] = {
                            "first_name": data[1],
                            "last_name": data[2],
                            "dob": data[3],
                            "email": data[4],
                            "username": data[5],
                            "password": data[6],
                            "account_number": int(data[7]),
                            "account_type": data[8],
                            "balance": float(data[9]),
                            "is_active": bool(int(data[10]))
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Error parsing customer record: {data} ({e})")
                elif record_type == 'transaction':
                    try:
                        transaction_id = int(data[0])
                        sample_db["transactions"][transaction_id] = {
                            "account_number": int(data[1]),
                            "transaction_type": data[2],
                            "date": data[3],
                            "amount": float(data[4]),
                            "balance_after": float(data[5])
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Error parsing transaction record: {data} ({e})")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return sample_db

def input_account_type():
    print("Choose your account type:")
    for idx, acc_type in enumerate(account_types, 1):
        print(f"\t{idx}. {acc_type}")
    while True:
        choice = input(">>>(1/2): ").strip()
        if choice in {'1', '2'}:
            return "savings" if choice == '1' else "current"
        print("Invalid choice. Please enter 1 or 2.")

def customer_inputs():
    sample_db = get_API()
    customer_data = {}
    customer_data['first_name'] = input("First Name: ").strip().capitalize()
    customer_data['last_name'] = input("Last Name: ").strip().capitalize()
    while True:
        dob_str = input("Date of Birth (YYYY-MM-DD): ").strip()
        try:
            datetime.datetime.strptime(dob_str, "%Y-%m-%d")
            customer_data['dob'] = dob_str
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
    customer_data['email'] = input("Email: ").strip().lower()
    customer_data['username'] = input("Username: ").strip()
    customer_data['password'] = input("Password: ").strip()
    customer_data['account_type'] = input_account_type()
    while True:
        try:
            balance = float(input("Initial Balance: "))
            customer_data['balance'] = balance
            break
        except ValueError:
            print("Invalid amount. Enter a number.")
    while True:
        active = input("Activate account? (y/n): ").strip().lower()
        if active in {'y', 'yes'}:
            customer_data['is_active'] = True
            break
        elif active in {'n', 'no'}:
            customer_data['is_active'] = False
            break
        else:
            print("Invalid input. Enter 'y' or 'n'.")
    customer_id = max(sample_db["customers"].keys(), default=1000) + 1
    print(f"Your Customer ID is: {customer_id}")
    account_number = int('4432' + str(customer_id))
    customer_data['account_number'] = account_number
    print(f"Your Account Number is: {account_number}")
    print("Now use your login credentials to login to HSBC Banking")
    return {customer_id: customer_data}

def register_customer():
    print("Create a HSBC Account.")
    print("Account in just 2 minutes. Fill the following form.")
    new_customer = customer_inputs()
    db = get_API()
    db['customers'].update(new_customer)
    return post_API(db)

def admin_main(loged_user):
    print("Your menu: ")
    print("1. See Login Details ")
    print("2. list all customers ")
    print("3. remove a customer")
    print("4. add admin")
    print("5. Logout")
    try:
        option = int(input(">>> "))
    except ValueError:
        print("Please enter a number.")
        return
    if option == 1:
        print("\tYour Personal Details: ")
        print("\tAdmin Id: ", loged_user[0], "\t\t| User Type: Admin")
        print("\tFirst Name: ", str(loged_user[1]).capitalize(), "\t| LastName:", str(loged_user[2]).capitalize())
        print("\tE-mail: ", loged_user[3])
        print("\tUsername: ", str(loged_user[4]), "\t| Password: ", str(loged_user[5]).removesuffix('\n'))
    elif option == 2:
        print('1. See Customers')
        print('2. See Transactions')
        try:
            op = int(input(">>> "))
        except ValueError:
            print("Please enter a number.")
            return
        if op == 1:
            format_str = "{:^10}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^15}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^10}\t| {:^10}"
            data_fields = ['Customer Id', 'First Name', 'Last Name', 'Date of Birth', 'E-mail', 'Username', 'Password', 'Account Number', 'Account Type', 'Balance']
            print(format_str.format(*data_fields))
            print("-"*150)
            for i in get_data('c'):
                print(format_str.format(*i))
            print("-"*150)
        elif op == 2:
            format_str = "{:^15}\t| {:^15}\t| {:^15}\t| {:^15}\t| {:^10}\t"
            data_fields = ['Transaction Id', 'Account Number', 'Transaction Type', 'Transaction Date','Amount']
            print(format_str.format(*data_fields))
            print("-"*150)
            for i in get_data('t'):
                print(format_str.format(*i))
            print("-"*150)
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        main()
    else:
        print("Choose right option please.")

def customer_main(loged_customer):
    print("Hello, ", str(loged_customer[1]).capitalize())
    print(f"Welcome to HBMS, Manage your | {loged_customer[8].upper()} | Account.")
    print()
    print("------------------------------------")
    print(f"\tYOU HAVE: £{loged_customer[9]}")
    print("------------------------------------")
    print("Choose your option: ")
    print("1. Check account details and update")
    print("2. Transaction history")
    print("3. All Accounts")
    print("4. Login Details and update")
    print("5. Make transactions")
    print("6. Logout")
    option = input(">>> ")
    if option == '1':
        print("\tYour Personal Details: ")
        print("-----------------------------------------------------------------")
        print(f"\tCustomer Id: {loged_customer[0]}\t| customer Type: Customer")
        print(f"\tFirst Name: {str(loged_customer[1]).capitalize()}\t| LastName: {str(loged_customer[2]).capitalize()}")
        print(f"\tDate of Birth: {loged_customer[3]} E_mail: {loged_customer[4]}")
        print(f"\tUsername: {str(loged_customer[5])}\t| Password: {loged_customer[6]}")
        print(f"\Account Number: {loged_customer[7]}\t| Account Type: {loged_customer[8]}")
        print("-----------------------------------------------------------------")
        update = input("Do you want to update?(y/n) ")
        if update == 'y':
            print("Update your Details ")
        else:
            print("Go to main")
    elif option == '2':
        format_str = "{:^10}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^15}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^10}\t| {:^10}"
        print("_"*120)
        data_fields = ['Transaction ID', 'Account Number', 'Transaction Date', 'Amount', 'E_mail', 'Username', 'Password', 'Account Number', 'Account Type', 'Balance']
        print("_"*120)
        print(format_str.format(*data_fields))
        for i in get_data('t'):
            print(format_str.format(*i))
            print("_"*120)
    elif option == '3':
        pass
    else:
        main()

def main():
    print("HSBC Bank Management System (HBMS)")
    print("Choose: ")
    print("\t1. if you are a customer.")
    print("\t2. if you are a admin.")
    print()
    try:
        sign = int(input(">>> "))
    except ValueError:
        print("Plese only enter number")
        return
    if sign == 1:
        print("Welcome Customer, to HBMS.")
        print("Choose: ")
        print("\t1. to Login, if you have account.")
        print("\t2. to Register, if you don't have account to.")
        try:
            option = int(input(">>> "))
        except ValueError:
            print("Please enter a number.")
            return
        if option == 1:
            print("Hello Customer, nice to see you. ")
            username = input("Username: ")
            password = input("Password: ")
            customer_list = get_data('c')
            for customer in customer_list:
                if customer[5] == username and  customer[6] == password:
                    print("You are good to go.")
                    customer_main(customer)
                    break
            else:
                print("User not found.")
        elif option == 2:
            register_customer()
    elif sign == 2:
        print("How are you admin? Login to your account.")
        username = input("Username: ")
        password = input("Password: ")
        admin_list = get_data('a')
        for admin in admin_list:
            if admin[4] == username and  str(admin[5]).removesuffix('\n') == password:
                print("You are good to go.")
                admin_main(admin)
                break
        else:
            print("User not found.")
    elif sign == 3:
        exit()
    else:
        print("Please Enter 1 or 2.")
    if input("Do want to exit?(y/n): ").strip().lower() == 'y':
        print("\n\n")

if __name__ == "__main__":
    main()
