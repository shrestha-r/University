# def prime(x, y):
#     prime_list = []
#     for i in range(x, y):
#         if i == 0 or i == 1:
#             continue
#         else:
#             for j in range(2, int(i/2)+1):
#                 if i % j == 0:
#                     print()
#             else:
#                 prime_list.append(i)
#     return prime_list


# # Driver program
# starting_range = 1
# ending_range = 100
# lst = prime(starting_range, ending_range)
# if len(lst) == 0:
#     print("There are no prime numbers in this range")
# else:
#     print("The prime numbers in this range are: ", lst)

num = int(input("Enter a number: "))
for i in range(2,100):
    if num == i:
        continue
    elif num %i == 0:
        print("It is not prime")
        break
    else:
        print("Prime number")
        break