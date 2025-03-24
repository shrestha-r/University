# 1. Create a function that takes a list of strings and returns the
# list sorted alphabetically.

def sorted_list(s_list):
    list.sort()
    return s_list
list = ['air', 'bf', 'dr','apple','cat', 'gf', 'mrs', 'ms']
new_list = sorted_list(list)
print(new_list)

# 3. Given a list of numbers, find the sum and average of using
# built-in functions.

def sum_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
def avg_list(list):
    return sum_list(list)/len(list)

list = [2,4,6,8,10]
sum = sum_list(list)
avg = avg_list(list)
print("sum of list is ", sum)
print("Average of list is ",avg)

# 6. Write a program that finds the largest and smallest elements
# in a list.

list = [5,3,3,4,10,44,66,1,2222,100,333]

great=list[0]
low = list[0]
for i in range(len(list)):
    if great < list[i]:
        great = list[i]
    if low > list[i]:
        low = list[i]

print("In list ",list)
print("largest number is ",great)
print("Smallest number is ",low)