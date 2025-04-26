def insertion_list(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        print("_____")
        print(j)
        previous = array[j]
        while j >=0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1
            print(j)
        print("--------")
        print(j)
        array[j+1] = key
    return array



list = [12,7,10,3,15,8,1]
sorted_list = insertion_list(list)
print(sorted_list)