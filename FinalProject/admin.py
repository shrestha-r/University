from getdata import get_data
from main import main
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
        print("_________________________________________________________")
        print("\tAdmin Id: ",loged_user[0],"\t\t| User Type: Admin")
        print("\tFirst Name: ",str(loged_user[1]).capitalize(),"\t| LastName:", str(loged_user[2]).capitalize())
        print("\tE_mail: ",loged_user[3])
        print("\tUsername: ",str(loged_user[4]),"\t| Password: ",str(loged_user[5]).removesuffix('\n'))
    elif option == 2:
        print('1. See Customers')
        print('2. See Transactions')
        op = int(input(">>> "))
        if op == 1:
            format_str = "{:^10}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^15}\t| {:^10}\t| {:^10}\t| {:^15}\t| {:^10}\t| {:^10}"
            data_fields = ['Customer Id', 'First Name', 'Last Name', 'Date of Birth', 'E_mail', 'Username', 'Password', 'Account Number', 'Account Type', 'Balance']
            print("______________________________________________________________________________________________________________________________________________________________________________________")
            print(format_str.format(*data_fields))
            print("______________________________________________________________________________________________________________________________________________________________________________________")
            for i in get_data('c'):
                i[9] = i[9].removesuffix('\n')
                print(format_str.format(*i))
                print("______________________________________________________________________________________________________________________________________________________________________________________")
            
        elif op == 2:
            format_str = "{:^15}\t| {:^15}\t| {:^15}\t| {:^15}\t| {:^10}\t| {:^10}\t"
            data_fields = ['Transaction Id', 'Account Number', 'Transaction Type', 'Transaction Date','Amount',"Balance"]
            print("_____________________________________________________________________________________________________________________")
            print(format_str.format(*data_fields))
            print("_____________________________________________________________________________________________________________________")
            for i in get_data('t'):
                i[5] = i[5].removesuffix("\n")
                print(format_str.format(*i))
                print("_____________________________________________________________________________________________________________________")
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        main()
    else:
        print("Choose right option please.")
admin_main(['3', 'bob', 'johnson', 'bob.j@email.com', 'admin3', 'bobpass\n'])