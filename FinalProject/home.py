from main import register_customer, admin_main
from getdata import get_data

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
        option = input(">>> ")
        if option == 1:
            #pass user in data? 
            pass
        elif option == 2:
            register_customer()
    elif sign == 2:
        print("How are you admin? Login to your account.")
        username = input("Username: ")
        password = input("Password: ")
        admin_list = get_data('a')
        for admin in admin_list:
            if admin[4] == username and  str(admin[5]).removesuffix('\n') == password:
                print(str(admin[5]))
                print("Hi ",admin[1])
                admin_main()
                print("You are good to go.")
    else:
        print("Please Enter 1 or 2.")

# admin;2|Alice|Smith|alice.smith@email.com|admin2|alicepwd