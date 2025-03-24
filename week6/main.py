'''
python is strange, you can not change the global value in local scope 
'''


# total = 0
# def sum(arg1,arg2):
#     total = arg1+arg2
#     print("inside the function local toal: ", total)
#     return total
# sum(10,20)
# print("Outside the function global total",total)
# global total = 0
# x = 0
# def myFun(x):
#     x = [20,30,40]
#     print(x)
# list = [10,11,12,13,14,15]
# myFun(list)
# print(list)



# def swap(x,y):
#     temp = x
#     x= y
#     y = temp

# x = 2
# y = 3
# swap(x,y)
# print(x)
# print(y)

#  function inside function non local variable
# def my_funct():
#     name = "joe"
#     def new_funct():
#         print(name)
#     new_funct()
# my_funct()


# global variable
# global value can not be change from local scope

x =200
x = x + 100
def myfunct():
    x = 10
    x = x+ 100
    print("Inside fucntion x = ",x)
myfunct()
print("Outside x = ",x)