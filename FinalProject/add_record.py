from getdata import get_data
sample_db = {
    "admins": [
        {
            "id": 1,
            "first_name": "john",
            "last_name": "doe",
            "email": "john.doe@email.com",
            "username": "admin1",
            "password": "pass123"
        },
        {
            "id": 2,
            "first_name": "alice",
            "last_name": "smith",
            "email": "alice.smith@email.com",
            "username": "admin2",
            "password": "alicepwd"
        },
        {
            "id": 3,
            "first_name": "bob",
            "last_name": "johnson",
            "email": "bob.j@email.com",
            "username": "admin3",
            "password": "bobpass"
        },
        {
            "id": 4,
            "first_name": "maria",
            "last_name": "garcia",
            "email": "maria.g@email.com",
            "username": "admin4",
            "password": "mariapw"
        },
        {
            "id": 5,
            "first_name": "david",
            "last_name": "lee",
            "email": "david.lee@email.com",
            "username": "admin5",
            "password": "davidpw"
        }
    ],
    "customers": [
        {
            "id": 1001,
            "first_name": "jane",
            "last_name": "smith",
            "dob": "1990-01-01",
            "email": "jane.smith@email.com",
            "username": "janes1",
            "password": "pass1234",
            "account_number": "12345678",
            "account_type": "savings",
            "balance": 5000.0
        },
        {
            "id": 1002,
            "first_name": "tom",
            "last_name": "brown",
            "dob": "1985-05-12",
            "email": "tom.brown@email.com",
            "username": "tomb2",
            "password": "tom12345",
            "account_number": "23456789",
            "account_type": "current",
            "balance": 200.0
        },
        {
            "id": 1003,
            "first_name": "sara",
            "last_name": "davis",
            "dob": "1992-07-23",
            "email": "sara.davis@email.com",
            "username": "sarad3",
            "password": "sara1234",
            "account_number": "34567890",
            "account_type": "savings",
            "balance": 0.0
        },
        {
            "id": 1004,
            "first_name": "mike",
            "last_name": "wilson",
            "dob": "1988-11-30",
            "email": "mike.w@email.com",
            "username": "mikew4",
            "password": "mike1234",
            "account_number": "45678901",
            "account_type": "current",
            "balance": 1000.0
        },
        {
            "id": 1005,
            "first_name": "linda",
            "last_name": "martinez",
            "dob": "1995-03-15",
            "email": "linda.m@email.com",
            "username": "lindam5",
            "password": "linda123",
            "account_number": "56789012",
            "account_type": "savings",
            "balance": 1000.0
        }
    ],
    "transactions": [
        {
            "transaction_id": 5001,
            "account_number": "12345678",
            "transaction_type": "deposit",
            "date": "2025-04-23",
            "amount": 100.0
        },
        {
            "transaction_id": 5002,
            "account_number": "12345678",
            "transaction_type": "withdrawal",
            "date": "2025-04-23",
            "amount": 2000.0
        },
        {
            "transaction_id": 5003,
            "account_number": "23456789",
            "transaction_type": "deposit",
            "date": "2025-04-22",
            "amount": 300.0
        },
        {
            "transaction_id": 5004,
            "account_number": "34567890",
            "transaction_type": "withdrawal",
            "date": "2025-04-21",
            "amount": 400.0
        },
        {
            "transaction_id": 5005,
            "account_number": "45678901",
            "transaction_type": "deposit",
            "date": "2025-04-20",
            "amount": 8.0
        },
        {
            "transaction_id": 5006,
            "account_number": "56789012",
            "transaction_type": "deposit",
            "date": "2025-04-19",
            "amount": 5000.0
        }
    ]
}
sample_db["admins"]
def add_record(dictionary_data):
    get_data()