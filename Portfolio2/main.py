dec_values = '0123456789'
bin_values = '01'
oct_values = '01234567'
hex_values = '0123456789ABCDEF'
num_system_values = [dec_values,bin_values,oct_values,hex_values]

def isCorrect(base=1,number=53):
    for i in range(len(number)):
        if number[i] not in num_system_values[base]:
            return False
    return True
def division_convert(base,number): #decimal number to any system
    number = int(number)
    original = int(number)
    answer = ''
    if base <= 1:
        return "Base should be greater than 1."
    if number == 0:
        return '0'
    print("\nSTEPS:")
    while number > 0: # when quotient become 0 loop end
        reminder = number%base
        if base == 16 and reminder>9 and reminder<17:
            reminder = hex_values[reminder]

        answer = str(reminder) + answer # reversing the string
        print(f"\t|\t{number} / {base} = {number // base} | {number%base}")
        print("\t------------------------------------")
        number = number // base # calculating quotient and updating quotient
    print("WRITE REMINDERS FROM DOWN TO TOP")
    print(f"({original}){10} = ({answer}){base}")
    return answer
    # return '('+answer+')'+str(base)
# ans = division_convert(2,4)
# print("Ans is ",ans)
def multiply_convert(base,number):
    reverse_binary = str(number).upper()[::-1]
    answer = 0
    i = 0
    print()
    lhs = ''
    for bit in reverse_binary:
        if base == 16:
            bit = hex_values.index(bit)
        answer += int(bit)*(pow(base,i))  
        print(f"Step {i+1}")
        print(f"{int(bit)} X {base}^{i} = {int(bit)*(pow(base,i))}")
        lhs = lhs + str(int(bit)*(pow(base,i))) + ' + '
        i +=1
    print(f"Step {i+1}\n{lhs.removesuffix(' + ')} = {answer}")
    return answer

def BitBit(bits=3,binary=1):
    bstring= str(binary)
    l = len(bstring)
    zeroToAdd = ((l//bits)+1)*bits
    print(zeroToAdd)
    ans= ''
    bstring = bstring.zfill(zeroToAdd)
    print(bstring)
    for i in range(0,zeroToAdd//bits):
        bit = bstring[bits*(i):(bits*(i+1))]
        ans += str(multiply_convert(2,int(bit)))
    print(ans)
    return ans
    
def menu():
    print("=================NUMBER SYSTEM=================")
    print("\t1. DECIMAL CONVERSION")
    print("\t2. BINARY CONVERSION")
    print("\t3. OCTAL CONVERSION")
    print("\t4. HEXADECIMAL CONVERSION")
options= '1234'
def main():
    menu()
    option = input("\tCHOOSE YOUR OPTION: ")
    if option in str(options):
        if int(option) == 1:
            number = int(input("Number: "))
            base = int(input("Base of Number: "))
            division_convert(base,number)
        elif int(option) == 2:
            base = int(input(" NUMBER BASE: "))
            number = int(input("NUMBER: "))
            print(multiply_convert(base,number))
        elif int(option) == 3:
            ...
        elif option == 4:
            ...
        elif option == 5:
            ...
        elif option == 6:
            ...
        elif option == 7:
            ...
        else:
            ...
    else:
        print("INVALID OPTION")
# octal_conversion = ['000','001','010','000','000','000']
# def digit_to_binary(digit):
# I will be using this function for bits = 3 or 4 
def bits_to_binary(bits, octal_number):
    binary = ''
    for i in octal_number:
        bit = str(division_convert(2,int(i))).zfill(bits)
        binary +=bit
    return binary

def decimal_conversion():
    print("\tCONVERSION FROM DECIMAL TO")
    print("\t1. BINARY")
    print("\t2. OCATAL")
    print("\t3. HEXADECIMAL")
    option = int(input("CHOOSE YOUR OPTION: "))
    decimal = (input("DECIMAL Number: ")).upper()
    if isCorrect(0,decimal):
        print("WELCOME ")
        # return "i'll be doing"
    else:
        print("Sorry But BYE")
        return "see you"
    if option == 1:
        division_convert(2,decimal)
    elif option == 2:
        division_convert(8,decimal)
    elif option == 3:
        division_convert(16,decimal)
    else:
        print("INVALID INPUT")
def binary_conversion():
    print("\tCONVERSION FROM DECIMAL TO")
    print("\t1. DECIMAL")
    print("\t2. OCATAL")
    print("\t3. HEXADECIMAL")
    binary = int(input("BINARY Number: "))
    option = int(input("CHOOSE YOUR OPTION: "))
    if option == 1:
        division_convert(2,binary)
    elif option == 2:
        multiply_convert(8,binary)
    elif option == 3:
        bits_to_binary(4,binary)
    else:
        print("INVALID INPUT")

def octal_conversiion():
    print("\tCONVERSION FROM DECIMAL TO")
    print("\t1. DECIMAL")
    print("\t2. BINARY")
    print("\t3. HEXADECIMAL")
    option = int(input("CHOOSE YOUR OPTION: "))
    octal = input("OCTAL Number: ")
    if isCorrect(2,octal):
        print("WELCOME ")
        # return "i'll be doing"
    else:
        print("Sorry But BYE")
        return "see you"
    if option == 1:
        # decimal 
        binary = multiply_convert(2,octal)
    elif option == 2:
        # binary 
        ans =  bits_to_binary(3,octal)
        print("Answer is ",ans)
    elif option == 3:
        # octal to hexadecimal 
        # first convert octal to binary 
        binary  = multiply_convert(2,octal)
        # 4 bits binary to hex 
        hex = bits_to_binary(4,binary)
        print(hex)
        
    else:
        print("INVALID INPUT")

def hexadecimal_conversion():
    print("\tCONVERSION FROM DECIMAL TO")
    print("\t1. DECIMAL")
    print("\t2. BINARY")
    print("\t3. OCATAL")
    option = int(input("CHOOSE YOUR OPTION: "))
    hexadecimal = input("ENTER HEXADECIMAL NUMBER: ")
    if isCorrect(3,hexadecimal):
        print("You are doing good")
    else:
        print("Soory")
        return "Sorry"
    if option == 1: # binary
        bits_to_binary(4,hexadecimal)
    elif option == 2:
        division_convert(8,hexadecimal)
    elif option == 3:
        multiply_convert(16,hexadecimal)
    else:
        print("INVALID INPUT")
# decimal_conversion()
# octal_conversiion()
# binary_conversion()
hexadecimal_conversion()

'''
instead of checking each number system, checking all number system by one function
'''
