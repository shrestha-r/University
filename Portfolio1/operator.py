import os
import time
first_name = 'rahul'
last_name = 'shrestha'
dob = 30122004
day = dob // 1000000
month = (dob//10000)%100
year = dob % 10000
phone_number = 0
email = ''
country_code = 0
account_number = str(25)+str(day)+str()
login_username = 'rahul20'
login_pin = 6373
os.system("clear")
print("====================MONZO MOBILE BANKING====================")
print(3)
print("\t\t Log In")
inputed_username = input("Username: ")
if inputed_username == login_username:
    inputed_pin = int(input("PIN: "))
    os.system("clear")
    print("====================MONZO BANKING====================")
    if inputed_pin == login_pin:
        print("Welcome Back :-)",first_name,last_name)
        print("press enter to continue")
        time.sleep(3)
        print("\tMAIN MENU")
        print("\t1.View Details")
        print("\t2.Check Balance")
        print("\t3.Send Money")
        print("\t4.Calculate Interest")
        print("\t5.Help")
        print("\t6.Exit")
        option = int(input("Select your options(1-6): "))
        if option == 1:
            print("View Your Details")
            print("=============================================")
            print("First Name: ", first_name,"Last Name: ",last_name)
            print("Date of Birth: ") 
            print(f"Day: {day} | Month: {month} | Year: {year}")
            print("Account No: ",)
            print("=============================================")
        elif option == 2:
            print("Check Balance")
        elif option == 3:
            print("Check Balance")
        elif option == 4:
            print("Check Balance")
        elif option == 5:
            print("Check Balance")
        elif option == 6:
            print("Check Balance")
        else:
            print("Invalid Input :-(")
    else:
        print("Incorrect PIN !!!") 
else:
    print("User not existed!")