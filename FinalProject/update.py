from getdata import get_data

def update_me(db_type, id,row):
    table = get_data()
    print(table)
    db = open("db.txt","w")
    if db_type == 'c':
        
    elif db_type == 'a':
        get_data('a')
    elif db_type == 't':
        get_data('t')
update_me()