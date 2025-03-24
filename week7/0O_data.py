# Data Structure 
'''
- List 
- Tuple 
- Dictionary 
- Set 
'''

'''
List 
ordered , changeable, duplicate, iterable
indexing start from 0 in computer science 
List methods 
- list = []
- insert()
- append()
- extend()
- remove()
- pop()
- clear()
- del()
'''

# code 1 
# print(len([1,2,3])) # length of list 
# print([1,2,3] + [4,5,6]) # comine 2 list 
# print(['Hi']*4) # repetition
# print(3 in [1,2,3]) # membership 
# for x in [1,2,3]: #iteration
#     print(x)

# output
'''
3
[1, 2, 3, 4, 5, 6]
['Hi', 'Hi', 'Hi', 'Hi']
True
1
2
3
'''

# code 2 

# numbers = [1,2,3,4,5,6,7,8,9]
# print(numbers[3:]) # return list with excluding first 3 elements
# print(numbers[1:4]) # start: end
# print(numbers[1:4:2]) # start :finish : steps 

# print(numbers[1::3]) # start : - : steps # just skip end



# code 3 for methods 
l = [1,2,3,4,5,6,7,8,9]
l.extend('string')
print(l)
# l.remove()

