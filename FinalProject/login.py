from getdata import get_data

def login(user_type, username, password):
    if user_type == 'a':
        admin_list = get_data(user_type)
        for admin in admin_list:
            if admin[4] == username:
                
                print(str(admin[5]))
                print("You are good to go.")
                return True 
        else:
            print("U")
    if user_type == 'c':
        get_data(user_type)


# admin;2|Alice|Smith|alice.smith@email.com|admin2|alicepwd
login('a','admin2','alicepwd')