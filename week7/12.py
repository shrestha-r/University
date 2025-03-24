# Given two dictionaries, merge them into a single dictionary.

A = {
    "name":"raja",
    "age":23,
    "address":"nuwakot"
}
B = {
    "name":"Soniya",
    "age":33,
    "address":"Kathmandu"
}
A.update(B)
print(A)