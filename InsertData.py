# InsertData.py
# Seeds sample data into an existing SQLite bank.db using execute() only.

import sqlite3

# Connect to local SQLite DB file in the working directory
conn = sqlite3.connect('bank.db')

# Enforce FOREIGN KEY constraints for this connection
conn.execute("PRAGMA foreign_keys = ON;")

cursor = conn.cursor()

# ---------------------------
# Customers
# ---------------------------
# NOTE: Keeping the original data exactly as provided.
# TODO: If the Zlatan email has a typo, change 'iamzlatam...' -> 'iamzlatan...'
cursor.execute("""
INSERT OR IGNORE INTO Customers (cust_id, name, address, email) VALUES
    (110, 'Lionel', 'Rosario', 'leomessi@gmail.com'),
    (111, 'Ronaldinho', 'Porto Alegre', 'ronaldinhogaucho10@gmail.com'),
    (112, 'Zlatan', 'Malmo', 'iamzlatamibrahimovic@gmail.com'),
    (113, 'Mario', 'Palermo', 'whyalwaysme45@gmail.com');
""")

# ---------------------------
# Accounts
# ---------------------------
cursor.execute("""
INSERT OR IGNORE INTO Accounts (acc_id, cust_id, acc_type, balance) VALUES
    (101, 110, 'Savings', 2500.00),
    (102, 111, 'Checking', 12000.00),
    (103, 112, 'Savings', 1500.00),
    (104, 113, 'Checking', 1700.00);
""")

# ---------------------------
# Transactions
# ---------------------------
cursor.execute("""
INSERT OR IGNORE INTO Transactions (trans_id, acc_id, trans_type, amount, date) VALUES
    (1, 101, 'deposit',    500.00, '2022-12-18'),
    (2, 102, 'withdrawal', 100.00, '2006-11-19'),
    (3, 103, 'deposit',    300.00, '2012-11-14'),
    (4, 104, 'withdrawal', 610.00, '2011-10-23'),
    (5, 102, 'deposit',    500.00, '2006-11-25'),
    (6, 103, 'withdrawal', 100.00, '2018-09-17'),
    (7, 104, 'deposit',    500.00, '2009-09-29'),
    (8, 104, 'withdrawal', 100.00, '2012-06-28');
""")

# Persist changes and close
conn.commit()
conn.close()
