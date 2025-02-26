# def login(username, age):
#     print("=======================")
#     print("Hello, ",username)
#     print("Welcome to MONZO.")

# login('raj',25)
# login('RAJKUMAR', 25)


# *args

# def print_lots(*names):
#     for name in names:
#         print("Hello ",name)

# print_lots("Rahul","Umesh", "Nafis")


# Good one 
# def sum(*nums):
#     sum = 0
#     for num in nums:
#         sum+=num
#     print("Sum of the numbers is ", sum)


# sum(1,2,3,5,6,7,8,9)
# sum(5,4,3,200)


#  PARAMS DISORDER
def my_function(st1, st2,st3):
    print("The best is: ",st2)

my_function("julia","max","Betty")

my_function(st3="Julia",st1="Max",st2="Betty")

# Default params

def welcomeUser(username="Guest"):
    print("Welcome",username)

welcomeUser("UMESH")
welcomeUser()


def mul_by_10(x=1):
    return x, x*10

ans = mul_by_10(2)
print(type(ans))
print(ans)