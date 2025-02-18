# Fixing logical errors

x = int(input("Enter number: "))

if x>10:
    print("above 10")
    if x >20:
        print("above 20")
else:
    print("but not above 20")

# fixed error 
if x>10:
    print("above 10")
    if x >20:
        print("above 20")
    else:
        print("but not above 20")