# Dictionary 

# student={
#     "name":"Rahul Shrestha",
#     "subjects":["Math","Software","Hardware","AES","P2P"],
#     "age":20,
#     "enrolled":True,
#     "fee_paid":True
# }
# print(student)



# Set 
# '''
# Unordered unchangleable unindexed 
# '''
# A = {1,2,3,4,5,6}
# B = {2,3,4,0,3,2,}
# print(A | B)

# Update 
# dict - dictionary.update(iterable)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# car.update({"color": "White"})
car.update()

print(car)


# set 

A = {1,2,3,4,5}
B = {3,2,34,7,66}
result = A | B
# result = A.update(B)
result = A.union(B)
A.update(B)
print(result)
print(A)