# def common(list1,list2):
#     common = []
#     for i in list1:
#         if i in list2:
#             if i not in common:
#                 common.append(i)
#     return common


#     return list


# list1 = [1,2,2,2,22,3,4]
# list2 = [2,2,3,2,3,3,4,7,9,5]

# l = common(list1,list2)
# print(l)


# 10. Implement a function that takes two lists and returns their
# union (all unique elements from both lists).
# def unique(list):
#     unique = []
#     for i in list:
#         if i not in unique:
#             unique.append(i)
#     return unique

# def union(list1,list2):
#     return unique(unique(list1) + unique(list2))
# list1 = [1,2,2,2,22,3,4]
# list2 = [2,2,3,2,3,3,4,7,9,5]
# union = union(list1,list2)
# print(union) 

# 9. Write a program that checks if a given list is sorted in
# ascending order

# def isSorted(list):
#     org = list
#     for i in range(len(list)-1):
#         if org[i] > org[i+1]:
#             return False
#     return True
# list = [1,3,2,3,4]
# print(isSorted(list))

# 8. create a python program that counts the occurrence of each
# element in a given list.
def occur(list):
    hash = []