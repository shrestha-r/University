# Question 1
# inch = float(input("Enter length in cm: "))
# cm  = inch * 2.54
# print(inch,"inch is equal to ",cm,"cm")


# Question 2
# km = float(input("Enter Weight in Kilogram: "))
# stone  = km * 0.157473
# print(km,"km is equal to ",stone,"stone")


# Question 3
# decimal = 0
# b0 = int(input("1st digit: "))
# decimal += b0 * pow(2,2)
# # print(decimal)
# b1 = int(input("2st digit: "))
# decimal += b1 * pow(2,1)
# # print(decimal)
# b2 = int(input("2st digit: "))
# decimal += b2 * pow(2,0)
# print(f"({str(b0)+str(b1)+str(b2)})2 = ",decimal)


# Question 4
# decimal = 0
# b0 = int(input("1st digit: "))
# decimal += b0 * pow(2,4)
# # print(decimal)
# b1 = int(input("2st digit: "))
# decimal += b1 * pow(2,3)
# # print(decimal)
# b2 = int(input("2st digit: "))
# decimal += 2 * pow(2,1)
# b3 = int(input("2st digit: "))
# decimal += b3 * pow(2,1)
# b4 = int(input("2st digit: "))
# decimal += b4 * pow(2,0)
# print(f"({str(b0)+str(b1)+str(b2)})2 = ",decimal)

# Question 5
binary = ''
decimal = int(input("Decimal number : "))
reminder = decimal % 2
binary += str(reminder)
answer = int(decimal/2)
reminder = answer%2 
binary += str(reminder+str(answer))

print(answer)


# print(answer)
# print(reminder)
print(binary)
# print(str(binary)[::-1])