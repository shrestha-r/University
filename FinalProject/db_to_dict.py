from pprint import pprint

sample_db = {
    "admins": {},
    "customers": {},
    "transactions": {}
}
with open('db.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue
    parts = line.split(';')
    record_type = parts[0]
    data = parts[1].split('|')
    
    if record_type == 'admin':
        admin_id = int(data[0])
        sample_db["admins"][admin_id] = {
            "first_name": data[1],
            "last_name": data[2],
            "email": data[3],
            "username": data[4],
            "password": data[5]
        }
    elif record_type == 'customer':
        customer_id = int(data[0])
        sample_db["customers"][customer_id] = {
            "first_name": data[1],
            "last_name": data[2],
            "dob": data[3],
            "email": data[4],
            "username": data[5],
            "password": data[6],
            "account_number": data[7],
            "account_type": data[8],
            "balance": float(data[9])
        }
    elif record_type == 'transaction':
        transaction_id = int(data[0])
        sample_db["transactions"][transaction_id] = {
            "account_number": data[1],
            "transaction_type": data[2],
            "date": data[3],
            "amount": float(data[4])
        }
pprint(sample_db)