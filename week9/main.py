# try:
#     print(age)
# except NameError:
#     print("There is an issues with your ")


# try: 
#     # print("hello")
#     print(age)
# except:
#     print("something")
# else:
#     print("nothing.")
# # finally:
#     # print("good question")



# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except NameError:
#     print("Variable age is not defined")
# except ValueError:
#     print("Waht you entered is not a nubmer")
#     print("try again")


while True:
    try:
        age = int(input("Enter age: "))
        print(age)
        break
    except NameError:
        print("Age is not defined")
    except ValueError:
        print("what you entered is not a number")
        print("try again")