# 8. create a python program that counts the occurrence of each
# element in a given list


list = [2,33,7,10,22,8,2,3,2,9,7,9,10,10,22,8,2,5,6,1,0]
list.sort()
A = set()
A.update(list)
print(A)
new_list = []
print(list)
dict = {}
for i in A:
    count = 0
    for j in range(len(list)):
        if i == list[j]:
            count +=1
    dict[i] = count

print(dict)
    