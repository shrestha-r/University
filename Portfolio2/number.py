# import click

'''
This are useful for checking, given number belogs to what?
'''

dec_values = '0123456789'
bin_values = '01'
oct_values = '01234567'
hex_values = '0123456789ABCDEF'
num_system_values = [dec_values,bin_values,oct_values,hex_values]
options= '12345'

# it will check correct or not?
# for dec=1 base=2,bin=3,oct=2,hex=4
def isCorrect(base, number):
    for i in range(len(number.upper())):
        if number[i] not in num_system_values[base-1]:
            return False
    return True
    
# want to continue:
def want_continue():
    option = input("Do you want to continue? \nif yes, press enter, else type exit: ")
    if option == "exit":
        return False
    return True
# DIVIDING NUMBER WITH BASE: For converting decimal number to any number
def division_convert(base,number):
    number = int(number)
    original = number
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
    print("WRITING REMINDERS FROM DOWN TO TOP")
    print(f"({original}){10} = ({answer}){base}")
    return answer

# multiplying by base and power from 0 to len of number
def multiply_convert(base,number):
    reverse_binary = str(number).upper()[::-1] # power is assign from right to left
    answer = 0
    i = 0
    print()
    lhs = ''
    for bit in reverse_binary:
        if base == 16:
            bit = hex_values.index(bit)
        answer += int(bit)*(pow(base,i))  
        print("|-------------------------------------------")
        print(f"|  Step {i+1}:")
        print(f"|\t{int(bit)} X {base}^{i} = {int(bit)*(pow(base,i))}")
        print("|-------------------------------------------")
        lhs = lhs + str(int(bit)*(pow(base,i))) + ' + '
        i +=1
    print("|-------------------------------------------")
    print(f"|  Step {i+1}:")
    print(f"|\t{lhs.removesuffix(' + ')} = {answer}")
    print(f"|\t({number})2 == ({answer})10")
    print("|--------------------------------------------")
    return answer

# convert hex/oct to bin bit by bit
def oct_bin(bits,number):
    number = str(number)
    ans = ''
    for i in number:
        i = hex_values.index(i)
        ans += str(division_convert(2,i)).zfill(bits)
    # print("Answer is ",ans)
    return ans

'''
wo this is something good, to explain 
1. arrange binary to 3 or 4 bbits 
2. then that each bits convert to bin
3. for hex, storing alphabet 
5. answer 
'''
def bin_to_hex(bits, binary):
    binary = str(binary)
    # print(binary)
    to_fill = bits*(len(binary)//bits + 1)
    if len(binary) <= bits or len(binary)%bits ==0:
        to_fill = len(binary)
    new_binary = (binary).zfill(to_fill) 
    print(f"{binary} == {new_binary}")
    ans = ''
    for i in range(0,len(new_binary),bits):
        bit = new_binary[i:bits+i]
        print(bit)
        bin_ans = multiply_convert(2,bit)
        print(bin_ans)
        if bits == 4:
            bin_ans = hex_values[bin_ans]
        ans += str(bin_ans)
    # print(ans)
    return ans

# Decimal Conversion
def decimal_conversion():
    # click.clear()
    print("\tCONVERSION FROM DECIMAL TO")
    decimal = (input("DECIMAL Number: ")).upper()
    print("\t1. BINARY")
    print("\t2. OCATAL")
    print("\t3. HEXADECIMAL")
    if not isCorrect(1,decimal):
        print("THIS IS NOT DECIMAL NUMBER.")
        print("PLEASE ENTER AGAIN!")
        decimal_conversion()
    else:
        option = int(input("CHOOSE YOUR OPTION: "))
        if option == 1:
            division_convert(2,decimal)
        elif option == 2:
            division_convert(8,decimal)
        elif option == 3:
            division_convert(16,decimal)
        else:
            print("INVALID INPUT")
            decimal_conversion()
# Binary Conversion 
def binary_conversion():
    # click.clear()
    print("\tCONVERSION FROM BINARY TO")
    binary = (input("BINARY Number: ")).upper()
    print("\t1. DECIMAL")
    print("\t2. OCATAL")
    print("\t3. HEXADECIMAL")
    if not isCorrect(2,binary):
        print("THIS IS NOT BINARY NUMBER.")
        print("PLEASE ENTER AGAIN!")
        binary_conversion()
    else:
        option = int(input("CHOOSE YOUR OPTION: "))
        if option == 1:
            multiply_convert(2,binary)
        elif option == 2:
            ans = bin_to_hex(3,binary)
            print('|---------------------------------------|')
            print(f"|({binary})2 == ({ans})8|")
            print('|---------------------------------------|')
        elif option == 3:
            ans = bin_to_hex(4,binary)
            print('|---------------------------------------|')
            print(f"|({binary})2 == ({ans})16|")
            print('|---------------------------------------|')
        else:
            print("INVALID INPUT")
            binary_conversion()
# Octal Conversion 
def octal_conversion():
    # click.clear()
    print("\tCONVERSION FROM OCTAL TO")
    octal = (input("OCTAL Number: ")).upper()
    print("\t1. DECIMAL")
    print("\t2. BINARY")
    print("\t3. HEXADECIMAL")
    if not isCorrect(3,octal):
        print("THIS IS NOT OCTAL NUMBER.")
        print("PLEASE ENTER AGAIN!")
        binary_conversion()
    else:
        option = int(input("CHOOSE YOUR OPTION: "))
        if option == 1:
            multiply_convert(8,octal)
        elif option == 2:
            ans = oct_bin(3,octal)
            print('|---------------------------------------|')
            print(f"|({octal})8 == ({ans})2|")
            print('|---------------------------------------|')
        elif option == 3:
            print("FIRST, CONVERTING TO BINARY")
            binary = oct_bin(3,octal)
            print("THEN, BINARY TO HEXADECIMAL")
            ans = bin_to_hex(4,binary)
            print('|---------------------------------------|')
            print(f"|({octal})8 == ({ans})16|")
            print('|---------------------------------------|')
        else:
            print("INVALID INPUT")
            octal_conversion()
# Hexadecimal Conversion 
def hexadecimal_conversion():
    # click.clear() #clear screen
    print("CONVERSION FROM HEXADECIMAL TO")
    hexadecimal = (input("HEXADECIMAL Number: ")).upper()
    print("\t1. DECIMAL")
    print("\t2. BINARY")
    print("\t3. OCTAL")
    if not isCorrect(4,hexadecimal):
        print("THIS IS NOT HEXADECIMAL NUMBER.")
        print("PLEASE ENTER AGAIN!")
        decimal_conversion()
    else:
        option = int(input("CHOOSE YOUR OPTION: "))
        if option == 1:
            multiply_convert(16,hexadecimal)
        elif option == 2:
            ans = oct_bin(4,hexadecimal)
            print('|---------------------------------------|')
            print(f"|({hexadecimal})16 == ({ans})2|")
            print('|---------------------------------------|')
        elif option == 3:
            binary = oct_bin(4,hexadecimal)
            ans = bin_to_hex(3,binary)
            print('|---------------------------------------|')
            print(f"|({hexadecimal})16 == ({ans})8|")
            print('|---------------------------------------|')
        else:
            print("INVALID INPUT")
            hexadecimal_conversion()

def menu():
    print("=================CONVERTIA- CONVERT INTO ALL=================")
    print("\t1. DECIMAL CONVERSION")
    print("\t2. BINARY CONVERSION")
    print("\t3. OCTAL CONVERSION")
    print("\t4. HEXADECIMAL CONVERSION")
    print("\t5. EXIT")
def main():
    menu()
    option = input("\tCHOOSE YOUR OPTION: ")
    if option in str(options):
        if int(option) == 1:
            while True:
                decimal_conversion()
                if not want_continue():
                    break
        elif int(option) == 2:
            while True:
                binary_conversion()
                if not want_continue():
                    break
        elif int(option) == 3:
            while True:
                octal_conversion()
                if not want_continue():
                    break
        elif int(option) == 4:
            while True:
                hexadecimal_conversion()
                if not want_continue():
                    break
        else:
            return False
        # click.clear()
        if input("PRESS ENTER FOR CONTINUE/ type exit to close program: ") == 'exit':
            print("THANK YOU FOR USING CONVERTIA- CONVERT INTO ALL")
            return False
    else:
        print("INVALID OPTION, CHOOSE YOUR OPTION WISELY")
        main()

while True:
    if not main():
        break
