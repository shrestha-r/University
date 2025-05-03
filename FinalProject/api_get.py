def get_API(record_type='all',filename='db.txt'):
    sample_db = {
        "admins": {},
        "customers": {},
        "transactions": {}
    }
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(';') # I will remove '\n' from the line
                record_type = parts[0]
                data = parts[1].split('|')
                print(data)
                
                if record_type == 'admin':
                    try:
                        admin_id = int(data[0])
                        sample_db["admins"][admin_id] = {
                            "first_name": data[1],
                            "last_name": data[2],
                            "email": data[3],
                            "username": data[4],
                            "password": data[5],
                            "is_superuser": bool(int(data[6]))
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Error with admin record: {data} ({e})")
                elif record_type == 'customer':
                    try:
                        customer_id = int(data[0])
                        sample_db["customers"][customer_id] = {
                            "first_name": data[1],
                            "last_name": data[2],
                            "dob": data[3],  # as string; parse if needed
                            "email": data[4],
                            "username": data[5],
                            "password": data[6],
                            "account_number": int(data[7]),
                            "account_type": data[8],
                            "balance": float(data[9]),
                            "is_active": bool(int(data[10]))
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Error with customer record: {data} ({e})")
                elif record_type == 'transaction':
                    try:
                        transaction_id = int(data[0])
                        sample_db["transactions"][transaction_id] = {
                            "account_number": int(data[1]),
                            "transaction_type": data[2],
                            "date": data[3],
                            "amount": float(data[4]),
                            "balance_after": float(data[5])
                        }
                    except (IndexError, ValueError) as e:
                        print(f"Error with transaction record: {data} ({e})")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    if record_type == 'c':
        return sample_db['customers']
    elif record_type == 'a':
        return sample_db["admins"]
    elif record_type == 't':
        return sample_db["transactions"]
    else:
        return sample_db
db = get_API()
print(db)
import datetime



def input_transaction(sample_db):
    transaction_data = {}
    transaction_id = max(sample_db['transactions'].keys(), default=5000) + 1
    while True:
        try:
            acc_num = int(input("Account Number: "))
            if any(cust['account_number'] == acc_num for cust in sample_db['customers'].values()):
                transaction_data['account_number'] = acc_num
                break
            else:
                print("No customer with this account number.")
        except ValueError:
            print("Invalid account number. Must be an integer.")
    while True:
        t_type = input("Transaction Type (deposit/withdrawal): ").strip().lower()
        if t_type in {'deposit', 'withdrawal'}:
            transaction_data['transaction_type'] = t_type
            break
        else:
            print("Invalid type. Choose 'deposit' or 'withdrawal'.")
    today = datetime.date.today()
    transaction_data['date'] = today
    print(f"Auto-set date: {today}")
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                transaction_data['amount'] = amount
                break
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount. Enter a number.")
    customer = next(cust for cust in sample_db['customers'].values() if cust['account_number'] == transaction_data['account_number'])
    if transaction_data['transaction_type'] == 'deposit':
        new_balance = customer['balance'] + transaction_data['amount']
    else:
        new_balance = customer['balance'] - transaction_data['amount']
    transaction_data['balance_after'] = new_balance
    print(f"Calculated balance after: {new_balance:.2f}")
    
    return {transaction_id: transaction_data}

# Example usage:
# sample_db = get_API()  # Load existing data
# new_customer = input_customer(sample_db)
# sample_db['customers'].update(new_customer)
# new_transaction = input_transaction(sample_db)
# sample_db['transactions'].update(new_transaction)
# post_API(sample_db)  # Save updated data

def register_customer():
    pass

sample_db = get_API()

# account_number = 


