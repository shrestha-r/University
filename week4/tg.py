print("Welcome to Huddersfield Vape Store")

print("Our Shops in shops are: ")
print("1. Strawberry Flavour")
print("2. Watermellon Flavour")
print("3. Mint Flavour")
print("4. Blue Berry Flavour")

option = int(input("Choose your option: "))
if option == 1:
    print("Strawberry Flavour options ")
    print(" 1. small size, $ 30")
    print(" 2. medium size, $ 35")
    print(" 3. large size, $ 40")
    print()
    size = int(input("Choose your option "))
    if size == 1:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"small Strawberry Flavour")
        print("Your amount is $",quantity*30)
    elif size == 2:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"medium Strawberry Flavour")
        print("Your amount is $",quantity*35)
    elif size == 3:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"large Strawberry Flavour")
        print("Your amount is $",quantity*40)
    else:
        print("Invalid Input !")
elif option == 2:
    print("Watermellon Flavour options ")
    print(" 1. small size, $ 35")
    print(" 2. medium size, $ 40")
    print(" 3. large size, $ 45")
    print()
    size = int(input("Choose your option "))
    if size == 1:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"small Watermellon Flavour")
        print("Your amount is $",quantity*35)
    elif size == 2:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"medium Watermellon Flavour")
        print("Your amount is $",quantity*40)
    elif size == 3:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"large Watermellon Flavour")
        print("Your amount is $",quantity*45)
    else:
        print("Invalid Input !")
elif option == 3:
    print("Mint Flavour options ")
    print(" 1. small size, $ 40")
    print(" 2. medium size, $ 45")
    print(" 3. large size, $ 50")
    print()
    size = int(input("Choose your option "))
    if size == 1:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"small Mint Flavour")
        print("Your amount is $",quantity*40)
    elif size == 2:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"medium Mint Flavour")
        print("Your amount is $",quantity*45)
    elif size == 3:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"Large Mint Flavour")
        print("Your amount is $",quantity*50)
    else:
        print("Invalid Input !")
elif option == 4:
    print("Blue Berry Flavour options ")
    print(" 1. small size, $ 50")
    print(" 2. medium size, $ 55")
    print(" 3. large size, $ 60")
    print()
    size = int(input("Choose your option "))
    if size == 1:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"small Blue Berry Flavour")
        print("Your amount is $",quantity*50)
    elif size == 2:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"medium Blue Berry Flavour")
        print("Your amount is $",quantity*55)
    elif size == 3:
        quantity = int(input("How many do you want? "))
        print("You choose ",quantity,"large Blue Berry Flavour")
        print("Your amount is $",quantity*60)
    else:
        print("Invalid Input !")
    print()
    print("Thank you for choosing our shop!")
else:
    print("Invalid Option ")