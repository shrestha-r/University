
# 1. Write a function to calculate the area of a circle given its radius.
# def circleArea(radius):
#     if radius < 0:
#         print("Sorry Can't be calculate")
#     elif radius == 0:
#         return 0
#     else:
#         return 3.14 * radius * radius
# print(circleArea(7))

# 2. Create a function that checks if a number is prime

# def isPrime(num):
#     num = abs(num)
#     for i in range(2,num): #num will not going to divide
#         if num % i == 0: # 
#             return False
#             # break
#     return True
# num = int(input("Enter a number: "))
# if isPrime(num) == True:
#     print("It is prime number.")
# elif num ==0 & num ==1 :
#     print("Neither Prime nor Not Prime")
# else:
#     print("This is not a prime number")

# 3. Implement a function that reverses a given string
# def reverseString(string):
#     reverse_string = ""
#     for i in range(len(string)-1, -1,-1):
#         reverse_string += string[i]
#     return reverse_string

# print(reverseString("hello"))
# print(reverseString("Good Boy You are "))
# print(reverseString("mom"))

# set = [30,50]
# print(set[0])
# 4. Given a list of numbers, create a function to find the sum of all positive numbers.

# def sum(*numbers):
#     sum = 0 
#     for num in numbers:
#         sum += num
#     return sum
# sum = sum(5,5,5,5)
# print(sum)

# 5. Write a python function to check if a given string is a palindrome.
# def isPalindrone(string):
#     if string == reverseString(string):
#         return True 
#     return False
# string = input("Enter a string: ")
# if isPalindrone(string):
#     print("This is a palindrome")
# else:
#     print("This is not palindrome")

# 6. Create a function to find the square of each element in a given list.
def listSquare(*numbers):
    square_list = []
    for i in numbers:
        square_list.append(i*i)
    return square_list
list = listSquare(3,2,1,5)
for i in list:
    print(i)


# 7. Implement a function that takes a number as input and prints its multiplication table.
def multiplicationTable(num):
    for i in range(10):
        print(num, " X ",i+1, ' == ', num*(i+1)) 
    
num = int(input("Enter number: "))
multiplicationTable(num)
# 8. Implement a function to check if a given year is a leap year or not.

def isLeapYear(year):
    if year < 0:
        print("Year must be a positive integer.")
        return False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("This is a leap year.")
                return True
            else:
                print("This is not a leap year.")
                return False
        else:
            print("This is a leap year.")
            return True
    else:
        print("This is not a leap year.")
        return False



# 9. Write a function to check if a number is even or odd and return “Even” or “Odd” accordingly.
def eventOdd(num):
    if num % 2 == 0:
        print(num, " is Even number")
    elif num == 0:
        print("The number is zero. ")
    else:
        print(num," is Odd number")

# 10. Create a function that takes a number as input and prints its multiplication table.