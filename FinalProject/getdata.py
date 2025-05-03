def get_data(data_type=''):
    admin_list = []
    customer_list = []
    transaction_list = []
    db = open('db.txt','r')
    all_data = db.readlines()
    db.close()
    for line_data in all_data:
        db_type = line_data.split(';')[0]
        data = line_data.split(';')[1].split("|")
        if db_type == 'admin':
            admin_list.append(data)
        elif db_type == 'customer':
            customer_list.append(data) 
        else:
            transaction_list.append(data)

    if data_type == 'a':
        return admin_list
    elif data_type == 'c':
        return customer_list
    elif data_type == 't':
        return transaction_list
    else:
        return all_data


# print(len(get_data('t')))
# print(get_data('t'))
# print(get_data('t'))
# print(get_data('t'))

db = open('db.txt','r')
db = db.read()
print(db.split(';'))
print(len(db))