from main import main
from getdata import get_data

def customer_main(loged_customer):
    print("Hello, ", str(loged_customer[1]).capitalize())
    print(f"Welcome to HDMS, Manage your | {loged_customer[8].upper()} | Account.")
    print()
    print("------------------------------------")
    print(f"\tYOU HAVE: £{loged_customer[9]}")
    print("------------------------------------")
    print("Choose your option: ")
    print("1. Check account details and update")
    print("2. Transaction history")
    # print("3. All Accounts")
    print("3. Login Details and update")
    print("4. Make transactions")
    print("5. Logout")
    option = int(input(">>> "))
    if option == 1:
        print("\tYour Personal Details: ")
        print("-----------------------------------------------------------------")
        print(f"\tAdmin Id: {loged_customer[0]}\t| customer Type: Admin")
        print(f"\tFirst Name: {str(loged_customer[1]).capitalize()}\t| LastName: {str(loged_customer[2]).capitalize()}")
        print(f"\tDate of Birth: {loged_customer[3]} E_mail: {loged_customer[4]}")
        print(f"\tUsername: {str(loged_customer[5])}\t| Password: {loged_customer[6]}")
        print(f"\Account Number: {loged_customer[7]}\t| Account Type: {loged_customer[8]}")
        print("-----------------------------------------------------------------")
        input == input("Do you want to update?(y/n) ")
        if input == 'y':
            print("Update your Details ")
        else:
            print("Go to main")

    elif option == 2:
        format_str = "{:^10}\t| {:^15}\t| {:^15}\t| {:^15}\t| {:^15}\t| {:^10}\t"
        print("________________________________________________________________________________________________________________________________")

        data_fields = ['Transaction ID', 'Account Number', 'Transaction Date', 'Amount', 'E_mail', 'Username', 'Password', 'Account Number', 'Account Type', 'Balance']

        print(format_str.format(*data_fields))
        print("________________________________________________________________________________________________________________________________")
        for i in get_data('t'):
            i[5] = i[5].removesuffix('\n')
            print(format_str.format(*i))
            print("________________________________________________________________________________________________________________________________")
    elif option == 3:
        pass
        main()
    else:
        print("Invalid Option.")
# (10) 
# hello = 'customer|1001|jane|smith|1990-01-01|jane.smith@email.com|janes1|pass1234|12345678|savings|5000.00'
# hi = hello.split('|')
# print(hi)

customer_main(['1001', 'jane', 'smith', '1990-01-01', 'jane.smith@email.com', 'janes1', 'pass1234', '12345678', 'savings', '5000.00'])