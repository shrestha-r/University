def word_count(string,word):
    list = string.split()
    return len(list)
    count = 0
    for i in list:
        if word == i:
            count += 1
    return count
        

string = "my name is rahul shrestha is name is "
x=word_count(string,"is")
print(x)