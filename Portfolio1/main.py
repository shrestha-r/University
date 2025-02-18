import os
import time
first_name = 'rahul'
last_name = 'shrestha'
dob = 30122004
phone_number = 0
email = ''
country_code = 0
login_username = 'rahul'
login_pin = 6373

print(first_name, "Welcome to Monzo Bank")
haveAccount = input("Do you have Bank Account?(y/n)")
if haveAccount == 'y' or haveAccount == 'yes':
    os.system("clear")
    time.sleep(2)
    print("Login Account to Our Monzo App")
    print()
    inputed_username = input("Username: ")
    inputed_pin = input("4 digit PIN: ")
    print("1. Personal Details 2. Login Details 3. See Amount 4. Deposit Amount ")
    
    if len(inputed_pin) == 4:
        if inputed_pin == login_pin:
            print("Welcome, User to Monzo App")
    else:
        print("you entered",len(inputed_pin),"Pin. \nplease enter 4 digit pin.")
elif haveAccount == 'n' or haveAccount == 'no':
    print("Create a new account")
    first_name = input("Enter first name: ")
    last_name  = input("Enter last name: ")
    dob = int(input("Enter DOB(dd/mm/year): ")) ## I will create a function to check dates 
    if len(str(dob)) == 8:
        day = dob // 1000000
        month = (dob//10000)%100
        year = dob % 10000
        if day<=31 and day >=1 and month <=12 and month >=1 and year >= 1900 and year <=2015:
            dob = str(day)+'-'+str(month)+'-'+str(year)
        else:
            print("There is an error with your DOB.")
            exit()
    else:
        print("Entered valid date of birth.",len(str(dob)))
    phone_number = int(input("Enter phone number: "))
    email = input("enter your email: ")
    country_code = int(input("Enter Country Code(44): "))

    print("###########################################")
    print("\t first name : ",first_name)
    print("\t first name : ",last_name)
    print("\t dob : ",dob)
    print("\t Phone Numbeer : ","+",country_code,phone_number)
    print("\t email : ",email)
    print("###########################################")
    check_details = input("You are accepting all details are correct by typing y or yes: ")

    if check_details == "yes" or check_details == "y":
        print("We are creating your Monzo Account......")
        time.sleep(3)
        print("############You Monzo Account created Successfully##############")
        account_no = str(25)+ str(ord(first_name[0]))+str(month)+str(day)+str(ord(last_name[0]))
        '''
        first_name[0] - it gives the first character of string provided by user
        ord() - it convert character into ascii code 
        str () - convert ascii code given by ord() to string so that we can combine other part of account_no
        '''
        print("Your account no. is ", account_no)
        login_username += last_name+str(day)
        print("Your username is ", login_username)
        print("###############################################")
        os.system("clear")
        print("Now create 4 digit PIN for ",login_username)
        login_pin = int(input("Enter PIN: "))
        if len(str(login_pin)) <4 and len(str(login_pin))>4:
            login_pin=int()
        else:
            print("Login pin set Successfully.")
            print("Your Username is ",login_username)
            print("Your")
    else:
        print("Sorry, account registration failed. Try Again.")
        exit()
else:
    print("Invalid Inputs!")
    print("you entered",haveAccount,", which is not allowed.")
    print("If you have account enter yes or y.")
    print("If you don't have account enter no or n.")