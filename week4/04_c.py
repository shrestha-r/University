# Write a Python program that accepts a string and calculate the number of digits and letters. Hint: explore isdigit() and isalphs() builtin functions. 
input_string = input("Enter a string: ")
num = 0
alpha = 0
for i in input_string:  
    try:
        print(int(i))
        num+=1
    except ValueError:
        alpha+=1

print("number",num)
print("char",alpha)