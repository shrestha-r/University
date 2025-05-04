import datetime

# Sample data for initialization
sample_data = '''admin;1|john|doe|john.doe@email.com|admin1|pass123|1
admin;2|alice|smith|alice.smith@email.com|admin2|alicepwd|1
admin;3|bob|johnson|bob.j@email.com|admin3|bobpass|0
admin;4|maria|garcia|maria.g@email.com|admin4|mariapw|0
admin;5|david|lee|david.lee@email.com|admin5|davidpw|0
customer;1001|jane|smith|1990-01-01|jane.smith@email.com|janes1|pass1234|12345678|savings|500.00|1
customer;1002|tom|brown|1985-05-12|tom.brown@email.com|tomb2|tom12345|23456789|current|200.00|1
customer;1003|sara|davis|1992-07-23|sara.davis@email.com|sarad3|sara1234|34567890|savings|1000.00|1
customer;1004|mike|wilson|1988-11-30|mike.w@email.com|mikew4|mike1234|45678901|current|0.00|0
customer;1005|linda|martinez|1995-03-15|linda.m@email.com|lindam5|linda123|56789012|savings|100.00|1
transaction;5001|12345678|deposit|2025-04-23|100.00|600.00
transaction;5002|12345678|withdrawal|2025-04-23|200.00|400.00
transaction;5003|23456789|deposit|2025-04-22|300.00|500.00
transaction;5004|34567890|withdrawal|2025-04-21|400.00|600.00
transaction;5005|45678901|deposit|2025-04-20|100.00|100.00
transaction;5006|56789012|deposit|2025-04-19|1000.00|1100.00
transaction;5007|45678901|withdrawal|2025-04-20|200.00|-100.00
'''
try:
    with open("db.txt", "r") as r:
        if r.read() == '':
            with open("db.txt", "w") as w:
                w.write(sample_data)
except FileNotFoundError:
    with open("db.txt", "w") as f:
        f.write(sample_data)

def post_API(sample_db, filename="db.txt"):
    with open(filename, 'w') as f:
        for admin_id, admin in sample_db['admins'].items():
            line = (
                f"admin;{admin_id}|{admin['first_name']}|{admin['last_name']}|"
                f"{admin['email']}|{admin['username']}|{admin['password']}|{int(admin['is_superuser'])}\n"
            )
            f.write(line)
        for customer_id, customer in sample_db['customers'].items():
            line = (
                f"customer;{customer_id}|{customer['first_name']}|{customer['last_name']}|{customer['dob']}|"
                f"{customer['email']}|{customer['username']}|{customer['password']}|{customer['account_number']}|"
                f"{customer['account_type']}|{customer['balance']:.2f}|{int(customer['is_active'])}\n"
            )
            f.write(line)
        for trans_id, trans in sample_db['transactions'].items():
            line = (
                f"transaction;{trans_id}|{trans['account_number']}|{trans['transaction_type']}|"
                f"{trans['date']}|{trans['amount']:.2f}|{trans['balance_after']:.2f}\n"
            )
            f.write(line)
    return get_API()

def get_API(record_type='all', filename='db.txt'):
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
                rec_type = parts[0]
                data = parts[1].split('|')
                if rec_type == 'admin':
                    admin_id = int(data[0])
                    sample_db["admins"][admin_id] = {
                        "first_name": data[1],
                        "last_name": data[2],
                        "email": data[3],
                        "username": data[4],
                        "password": data[5],
                        "is_superuser": bool(int(data[6]))
                    }
                elif rec_type == 'customer':
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
                elif rec_type == 'transaction':
                    transaction_id = int(data[0])
                    sample_db["transactions"][transaction_id] = {
                        "account_number": int(data[1]),
                        "transaction_type": data[2],
                        "date": data[3],
                        "amount": float(data[4]),
                        "balance_after": float(data[5])
                    }
    except FileNotFoundError:
        print(f"File {filename} not found.")
    if record_type == 'c':
        return sample_db['customers']
    elif record_type == 'a':
        return sample_db["admins"]
    elif record_type == 't':
        return sample_db["transactions"]
    else:
        return sample_db

def id_input():
    while True:
        try:
            id = int(input("Enter ID: "))
            return id
        except (ValueError, TypeError):
            print("Please enter correct ID.")

def input_choices(choices):
    print("Choose your account type:")
    for idx, choice in enumerate(choices, 1):
        print(f"\t{idx}. {choice}")
    while True:
        choice = input(f">>>1-{len(choices)}: ").strip()
        if choice in [str(i) for i in range(1, len(choices)+1)]:
            return choices[int(choice)-1]
        print(f"Invalid choice. Please number between 1 to {len(choices)}")

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
    customer_data['account_type'] = input_choices(["savings", "current"])
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

def add_admin():
    db = get_API()
    admin_data = {}
    admin_data['first_name'] = input("First Name: ").strip().capitalize()
    admin_data['last_name'] = input("Last Name: ").strip().capitalize()
    admin_data['email'] = input("Email: ").strip().lower()
    admin_data['username'] = input("Username: ").strip()
    admin_data['password'] = input("Password: ").strip()
    while True:
        is_superuser = input("Is Superuser? (y/n): ").strip().lower()
        if is_superuser in {'y', 'yes'}:
            admin_data['is_superuser'] = True
            break
        elif is_superuser in {'n', 'no'}:
            admin_data['is_superuser'] = False
            break
        else:
            print("Invalid input. Enter 'y' or 'n'.")
    admin_id = max(db["admins"].keys(), default=0) + 1
    db['admins'][admin_id] = admin_data
    post_API(db)
    print(f"Admin {admin_data['username']} added with ID {admin_id}.")

def display_customers():
    customers = get_API('c')
    format_str = "{:^10} | {:^10} | {:^10} | {:^12} | {:^20} | {:^10} | {:^10} | {:^12} | {:^10} | {:^10} | {:^8}"
    print(format_str.format("CustID", "First", "Last", "DOB", "Email", "Username", "Password", "Acct#", "Type", "Balance", "Active"))
    print("-"*130)
    for cid, c in customers.items():
        print(format_str.format(cid, c['first_name'], c['last_name'], c['dob'], c['email'], c['username'], c['password'], c['account_number'], c['account_type'], f"{c['balance']:.2f}", int(c['is_active'])))

def display_transactions():
    transactions = get_API('t')
    format_str = "{:^10} | {:^12} | {:^12} | {:^12} | {:^10} | {:^12}"
    print(format_str.format("TransID", "Acct#", "Type", "Date", "Amount", "BalAfter"))
    print("-"*80)
    for tid, t in transactions.items():
        print(format_str.format(tid, t['account_number'], t['transaction_type'], t['date'], f"{t['amount']:.2f}", f"{t['balance_after']:.2f}"))

def search_customer():
    customers = get_API('c')
    key = input("Search by (username/email/first_name/last_name): ").strip().lower()
    value = input("Enter value to search: ").strip().lower()
    found = False
    for cid, c in customers.items():
        if str(c.get(key, '')).lower() == value:
            print(f"Found: {cid} -> {c}")
            found = True
    if not found:
        print("No matching record found.")

def remove_customer():
    id = id_input()
    db = get_API()
    if id in db['customers']:
        db["customers"].pop(id)
        post_API(db)
        print(f"Record with id {id} has been removed from database.")
    else:
        print(f"Data with id {id} not found!")

def admin_main(admin_id, record):
    while True:
        print("\nAdmin Menu:")
        print("1. See Login Details")
        print("2. List all customers")
        print("3. Search for customer")
        print("4. See all transactions")
        print("5. Logout")
        if record["is_superuser"]:
            print("6. Add new admin")
            print("7. Remove a customer")
        option = input(">>> ")
        if option == '1':
            print(f"\nAdmin Id: {admin_id} | Name: {record['first_name']} {record['last_name']}")
            print(f"Email: {record['email']} | Username: {record['username']}")
            print(f"Is Superuser: {record['is_superuser']}")
        elif option == '2':
            display_customers()
        elif option == '3':
            search_customer()
        elif option == '4':
            display_transactions()
        elif option == '5':
            break
        elif option == '6' and record["is_superuser"]:
            add_admin()
        elif option == '7' and record["is_superuser"]:
            remove_customer()
        else:
            print("Invalid option or insufficient permissions.")

def customer_transaction(customer_id, customer):
    db = get_API()
    if not customer['is_active']:
        print("Account deactivated. Transactions disabled. You can only view details and history.")
        return
    while True:
        print("\nTransaction Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Back")
        option = input(">>> ")
        if option == '1':
            amt = float(input("Enter amount to deposit: "))
            customer['balance'] += amt
            db['customers'][customer_id]['balance'] = customer['balance']
            new_tid = max(db['transactions'].keys(), default=5000) + 1
            db['transactions'][new_tid] = {
                "account_number": customer['account_number'],
                "transaction_type": "deposit",
                "date": datetime.date.today().isoformat(),
                "amount": amt,
                "balance_after": customer['balance']
            }
            post_API(db)
            print(f"Deposited {amt:.2f}. New balance: {customer['balance']:.2f}")
        elif option == '2':
            amt = float(input("Enter amount to withdraw: "))
            if amt > customer['balance']:
                print("Insufficient funds.")
            else:
                customer['balance'] -= amt
                db['customers'][customer_id]['balance'] = customer['balance']
                new_tid = max(db['transactions'].keys(), default=5000) + 1
                db['transactions'][new_tid] = {
                    "account_number": customer['account_number'],
                    "transaction_type": "withdrawal",
                    "date": datetime.date.today().isoformat(),
                    "amount": amt,
                    "balance_after": customer['balance']
                }
                post_API(db)
                print(f"Withdrew {amt:.2f}. New balance: {customer['balance']:.2f}")
        elif option == '3':
            break
        else:
            print("Invalid option.")

def customer_main(customer_id, customer):
    while True:
        print(f"\nHello, {customer['first_name'].capitalize()}! | Account: {customer['account_type'].upper()} | Status: {'Active' if customer['is_active'] else 'Deactivated'}")
        print(f"Balance: £{customer['balance']:.2f}")
        print("1. View/Update Details")
        print("2. Transaction History")
        if customer['is_active']:
            print("3. Make Transaction")
            print("4. Logout")
        else:
            print("3. Logout")
        option = input(">>> ")
        if option == '1':
            print(f"\nCustomer Id: {customer_id}")
            print(f"Name: {customer['first_name']} {customer['last_name']}")
            print(f"DOB: {customer['dob']} | Email: {customer['email']}")
            print(f"Username: {customer['username']} | Password: {customer['password']}")
            print(f"Acct#: {customer['account_number']} | Type: {customer['account_type']}")
            print("Active:", "Yes" if customer['is_active'] else "No")
            if input("Update email or password? (y/n): ").strip().lower() == 'y':
                if input("Update email? (y/n): ").strip().lower() == 'y':
                    customer['email'] = input("New email: ").strip()
                if input("Update password? (y/n): ").strip().lower() == 'y':
                    customer['password'] = input("New password: ").strip()
                db = get_API()
                db['customers'][customer_id] = customer
                post_API(db)
                print("Details updated.")
        elif option == '2':
            transactions = get_API('t')
            print("\nYour Transactions:")
            for tid, t in transactions.items():
                if t['account_number'] == customer['account_number']:
                    print(f"{tid}: {t['transaction_type']} of {t['amount']} on {t['date']} (Balance after: {t['balance_after']})")
        elif option == '3' and customer['is_active']:
            customer_transaction(customer_id, customer)
        elif (option == '3' and not customer['is_active']) or (option == '4' and customer['is_active']):
            break
        else:
            print("Invalid option.")

def main():
    while True:
        print("\nHSBC Bank Management System (HBMS)")
        print("1. Customer")
        print("2. Admin")
        print("3. Register as Customer")
        print("4. Exit")
        try:
            sign = int(input(">>> "))
        except ValueError:
            print("Please enter a number.")
            continue
        if sign == 1:
            username = input("Username: ")
            password = input("Password: ")
            customers = get_API('c')
            for cid, c in customers.items():
                if c["username"] == username and c["password"] == password:
                    customer_main(cid, c)
                    break
            else:
                print("User not found or incorrect password.")
        elif sign == 2:
            username = input("Username: ")
            password = input("Password: ")
            admins = get_API('a')
            for aid, a in admins.items():
                if a["username"] == username and a["password"] == password:
                    admin_main(aid, a)
                    break
            else:
                print("Admin not found or incorrect password.")
        elif sign == 3:
            register_customer()
        elif sign == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
