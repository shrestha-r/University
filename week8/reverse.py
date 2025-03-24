def reverse_str(string):
    # return string[::-1]
    rev = ''
    # for i in range(1,len(string)):
    #     rev += string[-i]
    # return rev + string[0]

    for i in string:
        rev = i + rev
    return rev
print(reverse_str("hello"))

