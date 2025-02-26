# Write a porgram to generate the prime numbers from 1 to user defined range.
limit = int(input("Enter range from 1 to: "))
# print(2)
# count =0
# pirme_start = [2,3,5,7,11]
# for i in range(2    ,limit):
#     if i %2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%11:
#         print(i)
#         count+=1
# print(count)
# checkPrime = False

list = []
for i in range(1,limit):
    for j in range(1,15):
        if i %j !=0:
            list.append(i)
            break
print(list)
        