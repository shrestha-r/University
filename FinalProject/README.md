# HSBC Bank Management System (HBMS)

## Overview

The HSBC Bank Management System (HBMS) is a console-based application for managing bank accounts, users, and transactions. It supports multiple user roles (superuser admin, non-superuser admin, customer), enforces access control, and persists data in a flat file (`db.txt`). The system is designed for learning, prototyping, or small-scale administrative use.

---

## Features

- **Role-based access:** Superuser admin, non-superuser admin, customer
- **Customer registration and login**
- **Admin login**
- **View, search, and remove customers (superuser only)**
- **View customer and transaction records**
- **Customer account management**
- **Transaction history and basic transaction operations**
- **Data persistence using a text file**

---

## Data Model

### Database File: `db.txt`

Each line in the file represents a record of one of three types:

- **Admin:**  
  `admin;[id]|[first_name]|[last_name]|[email]|[username]|[password]|[is_superuser]`

- **Customer:**  
  `customer;[id]|[first_name]|[last_name]|[dob]|[email]|[username]|[password]|[account_number]|[account_type]|[balance]|[is_active]`

- **Transaction:**  
  `transaction;[id]|[account_number]|[transaction_type]|[date]|[amount]|[balance_after]`

---

## User Types and Permissions

| User Type            | Read Data | Write Data | Remove Customers | Add Admins | Make Transactions | Notes                                      |
|----------------------|:---------:|:----------:|:----------------:|:----------:|:-----------------:|---------------------------------------------|
| Superuser Admin      |     ✓     |     ✓      |        ✓         |     ✓      |        -          | Full database access                        |
| Non-superuser Admin  |     ✓     |     ✗      |        ✗         |     ✗      |        -          | Read-only access                            |
| Customer (Active)    |     ✓     |  Own only  |        -         |     -      |        ✓          | Can update own info and make transactions   |
| Customer (Inactive)  |     ✓     |  Own only  |        -         |     -      |        ✗          | Can only view info, no transactions allowed |

---

## Main Components

### Data Access Layer

- **`get_API(record_type, filename)`**  
  Loads and parses the database file, returning a dictionary of admins, customers, or transactions.

- **`post_API(sample_db, filename)`**  
  Writes the current in-memory database back to the file.

### User Input and Registration

- **`customer_inputs()`**  
  Prompts for customer registration details, validates, and returns a new customer record.

- **`register_customer()`**  
  Handles customer registration and persists the new record.

### Admin Operations

- **`admin_main(id, record)`**  
  Displays the admin menu and enforces superuser/non-superuser permissions for actions like removing customers or adding new admins.

### Customer Operations

- **`customer_main(logged_customer)`**  
  Displays the customer menu, allowing viewing/updating personal details, viewing transaction history, and making transactions (if active).

---

## Program Flow

1. **Startup:**  
   Loads or initializes the database file with sample data if empty.

2. **Main Menu:**  
   User chooses to log in as customer or admin, or to register as a new customer.

3. **Authentication:**  
   - Customers and admins are authenticated by username and password.
   - Admins are checked for superuser status for privileged actions.

4. **Role-based Menus:**  
   - Admins can view/search customers and transactions; superusers can also remove customers and add admins.
   - Customers can view/update their info, see transaction history, and (if active) make transactions.

5. **Data Persistence:**  
   All changes are written back to `db.txt` via the `post_API` function.

---

## Example Usage

### Registering a Customer

1. Run the program.
2. Choose "Customer" > "Register".
3. Enter your details as prompted.
4. Use your new credentials to log in.

### Admin Actions

- **Superuser:**  
  Can remove customers, add admins, view/search all records.
- **Non-superuser:**  
  Can only view/search records, no write operations.

### Customer Actions

- **Active:**  
  Can view/update info, see transactions, and perform deposits/withdrawals.
- **Inactive:**  
  Can only view personal details and transaction history.

---

## Extending the System

Potential enhancements include:
- Password hashing and security improvements
- Two-factor authentication
- Fund transfers between accounts
- PDF/CSV export of statements
- Audit log for admin actions
- More advanced search and reporting

---

## File Structure

- `db.txt` - Persistent storage for all records
- `paste.txt` - Source code file (as provided)
- All logic contained in a single Python script

---

## Running the Program

1. Ensure Python 3.x is installed.
2. Place the script and `db.txt` in the same directory.
3. Run the script:


4. Follow the on-screen prompts.

---

# HSBC Bank Management System (HBMS)  
**Documentation, Sample Data, and Table Relationships**

---

## Overview

The HSBC Bank Management System (HBMS) is a console-based application for managing bank accounts, users (admins and customers), and transactions. The system enforces role-based access and persists data in a flat file (`db.txt`) using three logical tables: Admin, Customer, and Transaction.

---

## Sample Data Tables

### **Admin Table**

| AdminID | First Name | Last Name | Email                   | Username | Password | IsSuperuser |
|---------|------------|-----------|-------------------------|----------|----------|-------------|
| 1       | john       | doe       | john.doe@email.com      | admin1   | pass123  | 1           |
| 2       | alice      | smith     | alice.smith@email.com   | admin2   | alicepwd | 1           |
| 3       | bob        | johnson   | bob.j@email.com         | admin3   | bobpass  | 1           |
| 4       | maria      | garcia    | maria.g@email.com       | admin4   | mariapw  | 1           |
| 5       | david      | lee       | david.lee@email.com     | admin5   | davidpw  | 1           |

---

### **Customer Table**

| CustomerID | First Name | Last Name | Date of Birth | Email                  | Username | Password | Account Number | Account Type | Balance | IsActive |
|------------|------------|-----------|---------------|------------------------|----------|----------|---------------|--------------|---------|----------|
| 1001       | jane       | smith     | 1990-01-01    | jane.smith@email.com   | janes1   | pass1234 | 12345678      | savings      | 500.00  | 1        |
| 1002       | tom        | brown     | 1985-05-12    | tom.brown@email.com    | tomb2    | tom12345 | 23456789      | current      | 200.00  | 1        |
| 1003       | sara       | davis     | 1992-07-23    | sara.davis@email.com   | sarad3   | sara1234 | 34567890      | savings      | 1000.00 | 1        |
| 1004       | mike       | wilson    | 1988-11-30    | mike.w@email.com       | mikew4   | mike1234 | 45678901      | current      | 0.00    | 1        |
| 1005       | linda      | martinez  | 1995-03-15    | linda.m@email.com      | lindam5  | linda123 | 56789012      | savings      | 100.00  | 1        |

---

### **Transaction Table**

| TransactionID | Account Number | Transaction Type | Date       | Amount  | Balance After |
|---------------|---------------|------------------|------------|---------|---------------|
| 5001          | 12345678      | deposit          | 2025-04-23 | 100.00  | 600.00        |
| 5002          | 12345678      | withdrawal       | 2025-04-23 | 200.00  | 400.00        |
| 5003          | 23456789      | deposit          | 2025-04-22 | 300.00  | 500.00        |
| 5004          | 34567890      | withdrawal       | 2025-04-21 | 400.00  | 600.00        |
| 5005          | 45678901      | deposit          | 2025-04-20 | 100.00  | 100.00        |
| 5006          | 56789012      | deposit          | 2025-04-19 | 1000.00 | 1100.00       |
| 5007          | 45678901      | withdrawal       | 2025-04-20 | 200.00  | -100.00       |

---

## Table Relationships Explained

### **1. Admin Table**
- Contains all admin users.
- Each admin is uniquely identified by `AdminID`.
- The `IsSuperuser` field determines if the admin has full write access (superuser) or is restricted to read-only actions (non-superuser)[4].

### **2. Customer Table**
- Contains all customer users.
- Each customer is uniquely identified by `CustomerID`.
- The `Account Number` field links each customer to their bank account.
- The `IsActive` field indicates if the customer can perform transactions (1 = active, 0 = inactive).

### **3. Transaction Table**
- Records all transactions performed in the system.
- Each transaction is uniquely identified by `TransactionID`.
- The `Account Number` field is a foreign key that links each transaction to a specific customer account[2][3][6].
- The `Transaction Type` can be deposit, withdrawal, etc.
- The `Amount` and `Balance After` fields track the transaction's value and resulting account balance.

---

### **Entity-Relationship (ER) Summary**

- **One-to-Many (1:N) between Customer and Transaction:**  
  Each customer (via their account number) can have zero or many transactions, but each transaction belongs to exactly one account[3][6].
- **Admins and Customers are separate entities:**  
  Admins manage the system but are not directly linked to accounts or transactions in this schema[4].
- **Transaction Table references Customer Table via Account Number:**  
  This allows easy retrieval of all transactions for a given customer/account[2][5][6].

#### **Diagram (Textual)**


## Notes

- All data is stored in plain text for simplicity.
- The system is for educational or prototyping use and should not be used in production without security enhancements.
