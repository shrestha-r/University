# Variables that will be used frequently 
admin_db = {"employee_id":"2025A01","first_name":"Rahul","last_name":"Shrestha","user_type":True}
# last_name = "middle_name + last_name"
customer_db = {"customer_id":"2025C0001","first_name":"Sandesh","last_name":"Kumar Bhagat","phone_number":7570732799,"gender":"male", "Address":"London"}
account_db = {"account_id":"20202020001","account_type":"current","date_opened":"20-10-2025","date_closed":"25-10-2026","status":True}
transaction_db = {"transaction_id":200001, "transaction_type":"deposit","amount":20.20,"transaction_date":"20-12-2022"}
database = {"admin_db":admin_db,"customer_db":customer_db,"account_db":account_db,"transaction_db":transaction_db}



db = open("database.txt","w")
db.write(str(database))
db.close()


def getLatestId():
    pass # will return id get from database

def register():
    pass
def login():
    print("Login to your Monzo Account")

def menu():
    pass
def main():
    menu()

main()