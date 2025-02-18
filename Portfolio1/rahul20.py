
first_name = 'rahul'
last_name = 'shrestha'
dob = 30122004
day = dob // 1000000
month = (dob//10000)%100
year = dob % 10000
phone_number = 0
email = ''
country_code = 977
account_no = 25330204
login_username = 'rahul20'
login_pin = 6373
balance = 50.50
import os
import time
os.system("clear")
print("====================MONZO MOBILE BANKING====================")
print("\t\t Log In")
inputed_username = input("Username: "   )
if inputed_username == login_username:
    inputed_pin = int(input("PIN: "))
    os.system("clear")
    print("====================MONZO MOBILE BANKING====================")
    if inputed_pin == login_pin:
        print("Welcome Back :-)",first_name,last_name)
        input("press enter to continue")
        print("\tMAIN MENU")
        print("\t1.View Details")
        print("\t2.Check Balance")
        print("\t3.Send Money")
        print("\t4.Reset PIN")
        print("\t5.Exit")
        option = int(input("Select your options(1-6): "))
        if option == 1:
            os.system("clear")
            print("View Your Details")
            print("=============================================")
            print("PERSONAL DETAILS")
            print("First Name: ", first_name," | Last Name: ",last_name)
            print("Date of Birth: ") 
            print(f"Day: {day} | Month: {month} | Year: {year}")
            input("press Enter: ")
            print("ACCOUNT DETAILS")
            print("Account No: ",account_no)
            print("Account Type: ","Current Account")
            print("Sort Code: 00-33-00")
            wantLoginView = input("DO you want to view login details?(y/n)")
            if wantLoginView == 'y':
                check_pin = int(input("Enter PIN: "))
                if check_pin == login_pin:
                    print("Username: ",login_username)
                    print("PIN: ",login_pin)
                    print("Thank", first_name, "Choosing Monzo. <3<3<3)")
                else:
                    print("Incorrect PIN. :-(")
            else:
                print("Thank", first_name, "Choosing Monzo. <3<3<3)")
            print("=============================================")
        elif option == 2:
            os.system("clear")
            print(f"Balance: \t : ${balance}")
            print("Thank", first_name, "Choosing Monzo. <3<3<3)")
        elif option == 3:
            os.system("clear")
            print("SEND YOUR MONEY")
            print("ADD Recipient")
            receiver_firstName = input("First Name:")
            receiver_lastName = input("Last Name:")
            receiver_sortCode = int(input("Sort Code(6 digit):"))
            receiver_AccountNo = int(input("Account Number(8 digit):"))
            if len(str(receiver_sortCode)) == 6 and len(str(receiver_AccountNo)) == 8:
                print("Checking Details") 
                time.sleep(3)
                print("Matched. :-)")
                amountToSend = float(input("Enter Amount $: "))
                print("checking your balance.")
                time.sleep(4)
                if amountToSend > balance:
                    print("A mount Exceed!!!.")
                    print("You have only $",balance)
                    print("Try Again!")
                    print("SEND NEXT TIME")
                    print("Thank", first_name, "Choosing Monzo. <3<3<3)")
                else:
                    print(":-):-) You have enough amount.")
                    print("Sending Money ......")
                    time.sleep(5)
                    print(f"${amountToSend} has been sent to Account no {receiver_AccountNo}. :-):-)")
                    print(f"you have only ${balance-amountToSend}")
                    print("Thank", first_name, "Choosing Monzo. <3<3<3)")
            else:
                print("Details did not match!")
                print("SEND NEXT TIME.")
                print("Thank", first_name, "Choosing Monzo. <3<3<3)")
        elif option == 4:
            os.system("clear")
            print("RESET YOUR PIN")
            previous_pin = int(input("Previous PIN: "))
            if previous_pin == login_pin:
                new_pin = int(input("New PIN: "))
                confirm_pin = int(input("Confirm PIN: "))
                if new_pin == confirm_pin:
                    login_pin = new_pin
                    print("YOUR PIN HAS BEEN CHANGED :-)")
                    print("Thank", first_name, "Choosing Monzo. <3<3<3)")
                else:
                    print("PIN NOT Matched (!=)")
                    print("TRY NEXT TIME")
                    print("Thank", first_name, "Choosing Monzo. <3<3<3)")
            else:
                print("PIN RESETTING FAILD.:-(")
                print("Thank", first_name, "Choosing Monzo. <3<3<3)")
        elif option == 5:
            os.system("clear")
            print("Thank", first_name, "Choosing Monzo. <3<3<3)")
            exit()
        else:
            print("Invalid Input :-(")
    else:
        print("Incorrect PIN !!!") 
else:
    print("User not existed!")
