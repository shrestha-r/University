from main import main
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
    print("3. All Accounts")
    print("4. Login Details and update")
    print("5. Make transactions")
    print("6. Logout")
    option = input(">>> ")
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    else:
        main()
# (10) 
hello = 'customer|1001|jane|smith|1990-01-01|jane.smith@email.com|janes1|pass1234|12345678|savings|5000.00'
hi = hello.split('|')
print(hi)

customer_main(['1001', 'jane', 'smith', '1990-01-01', 'jane.smith@email.com', 'janes1', 'pass1234', '12345678', 'savings', '5000.00'])