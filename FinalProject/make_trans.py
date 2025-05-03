import datetime

user = {1001: {
            'first_name': 'jane',
            'last_name': 'smith',
            'dob': datetime.date(1990, 1, 1),
            'email': 'jane.smith@email.com',
            'username': 'janes1',
            'password': 'pass1234',
            'account_number': 12345678,
            'account_type': 'savings',
            'balance': 500.0,
            'is_active': True
        }}
def input_transaction(loged_user, sample_db):
    transaction_data = {}
    transaction_id = max(sample_db['transactions'].keys(), default=5000) + 1
    # account_number from login user
    transaction_data['account_number'] = dict(loged_user).values().
    while True:
        t_type = input("Transaction Type (deposit/withdrawal): ").strip().lower()
        if t_type in {'deposit', 'withdrawal'}:
            transaction_data['transaction_type'] = t_type
            break
        else:
            print("Invalid type. Choose 'deposit' or 'withdrawal'.")
    transaction_data['date'] = datetime.date.today()
    while True:
        try:
            amount = float(input("Amount: "))
            if amount > 0:
                transaction_data['amount'] = amount
                break
            elif amount == 0:
                print("You can not do transaction of amount $ 0.")
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Invalid amount. Enter a number.")
    customer = customer
    if transaction_data['transaction_type'] == 'deposit':
        new_balance = customer['balance'] + transaction_data['amount']
    else:
        new_balance = customer['balance'] - transaction_data['amount']
    transaction_data['balance_after'] = new_balance
    print(f"Calculated balance after: {new_balance:.2f}")
    
    return {transaction_id: transaction_data}

def make_transaction():
