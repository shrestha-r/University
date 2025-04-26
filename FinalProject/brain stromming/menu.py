def menu_function():
    print("Welcome to MONZO APP")
    print("Manage your finance with your finger tip.")
    print("1. Login to your Account")
    print("2. Register to Monzo")
    for i in range(3):
        try:
            option = input(">>>")
            if option == '1':
                ...
                # login()
            elif option == '2':
                # register()
                ...
            else:
                raise Exception("Choose right option")
        except ValueError:
            print("Please enter correct option")
        except:
            print("Sorry, something is wrong.")