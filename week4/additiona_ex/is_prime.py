# def isPrime(number):
#     for i in range(2,number):
#         if number % i == 0:
#             # print(number," is not a prime number.")
#             return False
#             break
#         # print(number,"It is Prime number")
#         # break
#     return True


# while True:
#     check = isPrime(int(input("Enter a number")))
#     if check == True:
#         print("Prime number")
#     else:
#         print("Not a prime number")


limit = int(input("Prime number from 1- "))
count = 0
for i in range(0,limit+1):
    status = True
    if i == 0 or i == 1:
        continue
    else:
        for j in range(2,i):
            if i%j == 0:
                status = False
                break
            else:
                status = True
    if status == True:
        count+=1
        print(i, status)
print("There are ",count,"prime number between 1 to ",limit)