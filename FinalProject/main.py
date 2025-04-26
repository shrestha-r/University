## text file structues
'''
admin ; employee_id | first_name | last_name | email ; username | password
customer ; customer_id | first_name | last_name | email | dob ; user_id | pin_code; account_number | account_type | balance; transaction_id | transactin_type | transaction_date
'''

sample_data = '''admin;1|john|doe|john.doe@email.com|admin1|pass123
admin;2|alice|smith|alice.smith@email.com|admin2|alicepwd
admin;3|bob|johnson|bob.j@email.com|admin3|bobpass
admin;4|maria|garcia|maria.g@email.com|admin4|mariapw
admin;5|david|lee|david.lee@email.com|admin5|davidpw
customer;1001|jane|smith|1990-01-01|jane.smith@email.com|janes1|pass1234|12345678|savings|5000.00
customer;1002|tom|brown|1985-05-12|tom.brown@email.com|tomb2|tom12345|23456789|current|200.00
customer;1003|sara|davis|1992-07-23|sara.davis@email.com|sarad3|sara1234|34567890|savings|0.00
customer;1004|mike|wilson|1988-11-30|mike.w@email.com|mikew4|mike1234|45678901|current|1000.00
customer;1005|linda|martinez|1995-03-15|linda.m@email.com|lindam5|linda123|56789012|savings|1000.00
transaction;5001|12345678|deposit|2025-04-23
transaction;5002|12345678|withdrawal|2025-04-23
transaction;5003|23456789|deposit|2025-04-22
transaction;5004|34567890|withdrawal|2025-04-21
transaction;5005|45678901|deposit|2025-04-20
transaction;5006|56789012|deposit|2025-04-19
'''

# print(sample_data)
### file stored data 
try:
    r = open("db.txt","r")
    if r.read() == '':
       w = open("db.txt","w")
       w.write(sample_data) 
       w.close()
    r.close()
except FileNotFoundError:
    f = open("db.txt","w")
    f.write(sample_data)
### important variables 
account_types = ["Current Account","Saving Accoount", "Fixed Deposite"]

####  update database 
def update_database(update_data):
    pass
### utilities functions 
def get_data(data_type='c'):
    admin_list = []
    customer_list = []
    transaction_list = []
    db = open('db.txt','r')
    all_data = db.readlines()
    db.close()
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
def write_file(data):
    db = open('db.txt','w')
    data = db.write(data)



### need functions 
def login(db_type,username, password):
    if db_type == 'c':
        get_data(db_type)

def register_customer():
    print("Create a admin account")
def login_customer():
    print("Login Customer ")
def login_admin():
    print("Login Admin ")


# main GUI | interface of the program strats from here.
def admin_main(loged_user):
    print("Your menu: ")
    print("1. See Login Details ")
    print("2. list all customers ")
    print("3. remove a customer")
    print("4. add admin")
    print("5. Logout")
    option = int(input(">>> "))
    if option == 1:
        print("\tYour Personal Details: ")
        print("\tAdmin Id: ",loged_user[0],"\t\t| User Type: Admin")
        print("\tFirst Name: ",str(loged_user[1]).capitalize(),"\t| LastName:", str(loged_user[2]).capitalize())
        print("\tE-mail: ",loged_user[3])
        print("\tUsername: ",str(loged_user[4]),"\t| Password: ",str(loged_user[5]).removesuffix('\n'))
    elif option == 2:
        print('1. See Customers')
        print('2. See Transactions')
        op = int(input(">>> "))
        if op == 1:
            format_str = "{:^10}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^15}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^10}\t| {:^10}"
            data_fields = ['Customer Id', 'First Name', 'Last Name', 'Date of Birth', 'E-mail', 'Username', 'Password', 'Account Number', 'Account Type', 'Balance']
            print(format_str.format(*data_fields))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for i in get_data('c'):
                print(format_str.format(*i))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            
        elif op == 2:
            format_str = "{:^15}\t| {:^15}\t| {:^15}\t| {:^15}\t| {:^10}\t"
            data_fields = ['Transaction Id', 'Account Number', 'Transaction Type', 'Transaction Date','Amount']
            print(format_str.format(*data_fields))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            for i in get_data('t'):
                print(format_str.format(*i))
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        main()
    else:
        print("Choose right option please.")
def customer_main(loged_cutomer):
    print("Choose your option: ")
    print("1. Check account details and update")
    print("2. Transaction history")
    print("3. All Accounts")
    print("4. Login Details and update")
    print("5. Make transactions")
    print("6. Logout")
    option = input(">>> ")
    if option == 1:
        pass

# code will run from here .... 
def main():
    print("HSBC Bank Management System (HBMS)")
    print("Choose: ")
    print("\t1. if you are a customer.")
    print("\t2. if you are a admin.")
    print()
    try:
        sign = int(input(">>> "))
    except ValueError as e:
        print("Plese only enter number")
    else: 
        if sign == 1:
            print("Welcome Customer, to HBMS.")
            print("Choose: ")
            print("\t1. to Login, if you have account.")
            print("\t2. to Register, if you don't have account to.")
            option = int(input(">>> "))
            if option == 1:
                print("Hello Customer, nice to see you. ")
                username = input("Username: ")
                password = input("Password: ")
                customer_list = get_data('c')
                for customer in customer_list:
    # customer;1005|linda|martinez|1995-03-15|linda.m@email.com|lindam5|linda123|56789012|savings|1000.00
                    if customer[5] == username and  customer[6] == password:
                        print(customer)
                        print(str(customer[5]))
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
                    print(admin)
                    print(str(admin[5]))
                    print("You are good to go.")
                    admin_main(admin)
                else:
                    print("Wrong Credentials.")
            else:
                print("User not found.")
        elif sign == 3:
            exit()
        else:
            print("Please Enter 1 or 2.")
main()