accounts =   [{"Account Number": 1001,"Account Holder Name": "Alice Johnson","Account Type": "Savings","Balance": 1500.00,"Interest Rate": 1.5,"Transaction History": ["Deposited 500", "Withdrew 200"]}] 
with open('accounts.txt', 'w') as f:
    # Write header
    f.write("Account Number,Account Holder Name,Account Type,Balance,Interest Rate,Transaction History\n")
    for account in accounts:
        # Convert transaction history list to a string
        transactions = "; ".join(account["Transaction History"])
        line = f"{account['Account Number']},{account['Account Holder Name']},{account['Account Type']},{account['Balance']},{account['Interest Rate']},{transactions}\n"
        f.write(line)
