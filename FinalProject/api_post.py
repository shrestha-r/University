from api_get import get_API
import datetime

sample_db = {
    'admins': {
        1: {
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'john.doe@email.com',
            'username': 'admin1',
            'password': 'pass123',
            'is_superuser': True
        },
        2: {
            'first_name': 'alice',
            'last_name': 'smith',
            'email': 'alice.smith@email.com',
            'username': 'admin2',
            'password': 'alicepwd',
            'is_superuser': True
        },
        3: {
            'first_name': 'bob',
            'last_name': 'johnson',
            'email': 'bob.j@email.com',
            'username': 'admin3',
            'password': 'bobpass',
            'is_superuser': True
        },
        4: {
            'first_name': 'maria',
            'last_name': 'garcia',
            'email': 'maria.g@email.com',
            'username': 'admin4',
            'password': 'mariapw',
            'is_superuser': True
        },
        5: {
            'first_name': 'david',
            'last_name': 'lee',
            'email': 'david.lee@email.com',
            'username': 'admin5',
            'password': 'davidpw',
            'is_superuser': True
        }
    },
    'customers': {
        1001: {
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
        },
        1002: {
            'first_name': 'tom',
            'last_name': 'brown',
            'dob': datetime.date(1985, 5, 12),
            'email': 'tom.brown@email.com',
            'username': 'tomb2',
            'password': 'tom12345',
            'account_number': 23456789,
            'account_type': 'current',
            'balance': 200.0,
            'is_active': True
        },
        1003: {
            'first_name': 'sara',
            'last_name': 'davis',
            'dob': datetime.date(1992, 7, 23),
            'email': 'sara.davis@email.com',
            'username': 'sarad3',
            'password': 'sara1234',
            'account_number': 34567890,
            'account_type': 'savings',
            'balance': 1000.0,
            'is_active': True
        },
        1004: {
            'first_name': 'mike',
            'last_name': 'wilson',
            'dob': datetime.date(1988, 11, 30),
            'email': 'mike.w@email.com',
            'username': 'mikew4',
            'password': 'mike1234',
            'account_number': 45678901,
            'account_type': 'current',
            'balance': 0.0,
            'is_active': True
        },
        1005: {
            'first_name': 'linda',
            'last_name': 'martinez',
            'dob': datetime.date(1995, 3, 15),
            'email': 'linda.m@email.com',
            'username': 'lindam5',
            'password': 'linda123',
            'account_number': 56789012,
            'account_type': 'savings',
            'balance': 100.0,
            'is_active': True
        }
    },
    'transactions': {
        5001: {
            'account_number': 12345678,
            'transaction_type': 'deposit',
            'date': datetime.date(2025, 4, 23),
            'amount': 100.0,
            'balance_after': 600.0
        },
        5002: {
            'account_number': 12345678,
            'transaction_type': 'withdrawal',
            'date': datetime.date(2025, 4, 23),
            'amount': 200.0,
            'balance_after': 400.0
        },
        5003: {
            'account_number': 23456789,
            'transaction_type': 'deposit',
            'date': datetime.date(2025, 4, 22),
            'amount': 300.0,
            'balance_after': 500.0
        },
        5004: {
            'account_number': 34567890,
            'transaction_type': 'withdrawal',
            'date': datetime.date(2025, 4, 21),
            'amount': 400.0,
            'balance_after': 600.0
        },
        5005: {
            'account_number': 45678901,
            'transaction_type': 'deposit',
            'date': datetime.date(2025, 4, 20),
            'amount': 100.0,
            'balance_after': 100.0
        },
        5006: {
            'account_number': 56789012,
            'transaction_type': 'deposit',
            'date': datetime.date(2025, 4, 19),
            'amount': 1000.0,
            'balance_after': 1100.0
        },
        5007: {
            'account_number': 45678901,
            'transaction_type': 'withdraw',
            'date': datetime.date(2025, 4, 20),
            'amount': 200.0,
            'balance_after': -100.0
        }
    }
}
new = {5007:{
            'account_number': 45678901,
            'transaction_type': 'deposite',
            'date': datetime.date(2025, 4, 20),
            'amount': 3000.0,
            'balance_after': 3100.0
        }}
print(sample_db['customers'])
sample_db['transactions'].update(new)
print(len(sample_db['customers']))



def post_API(sample_db, filename="db.txt"):
    with open(filename, 'w') as f:
        # Write admins with is_superuser as int
        for admin_id, admin in sample_db['admins'].items():
            line = (
                f"admin;{admin_id}|{admin['first_name']}|{admin['last_name']}|"
                f"{admin['email']}|{admin['username']}|{admin['password']}|{int(admin['is_superuser'])}\n"
            )
            f.write(line)

        # Write customers with is_active as int
        for customer_id, customer in sample_db['customers'].items():
            line = (
                f"customer;{customer_id}|{customer['first_name']}|{customer['last_name']}|{customer['dob']}|"
                f"{customer['email']}|{customer['username']}|{customer['password']}|{customer['account_number']}|"
                f"{customer['account_type']}|{customer['balance']:.2f}|{int(customer['is_active'])}\n"
            )
            f.write(line)

        # Write transactions (no boolean fields)
        for trans_id, trans in sample_db['transactions'].items():
            line = (
                f"transaction;{trans_id}|{trans['account_number']}|{trans['transaction_type']}|"
                f"{trans['date']}|{trans['amount']:.2f}|{trans['balance_after']:.2f}\n"
            )
            f.write(line)
    return get_API()


print(post_API(sample_db))