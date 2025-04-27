# def login(username,password):
#     db = open("db.txt","r")
#     data = db.readlines()
#     for i in data:
#         db_type = i.split(';')
#         # print(db_type)
#         if db_type[0] == 'admin':
#             admin = db_type[1].split('|')
#             print(admin)
#             if admin[4] == username and admin[5] == password+'\n':
#                 print(admin[4])
#                 print(admin[5])
#                 return True

#     return "False"


# print(login('admin3','bobpass'))



demo = ['5002', '12345678', 'withdrawal', '2025-04-23', '200.00', '400.00\n']
five = demo[5].removesuffix("\n")
demo[5] = five
print(*demo)