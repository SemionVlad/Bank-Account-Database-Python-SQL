# createDB.py
# Creates the SQLite schema for a small bank DB using execute() only.

import sqlite3

# Connect to local SQLite DB file in the working directory
conn = sqlite3.connect('bank.db')

# Enforce FOREIGN KEY constraints for this connection
conn.execute("PRAGMA foreign_keys = ON;")

cursor = conn.cursor()

# ---------------------------
# Customers
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    cust_id INTEGER PRIMARY KEY,
    name    TEXT    NOT NULL,
    address TEXT,
    email   TEXT    UNIQUE
);
""")

# ---------------------------
# Accounts
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Accounts (
    acc_id   INTEGER PRIMARY KEY,
    cust_id  INTEGER NOT NULL,
    acc_type TEXT    NOT NULL CHECK (acc_type IN ('Savings','Checking')),
    balance  REAL    NOT NULL DEFAULT 0.0,
    FOREIGN KEY (cust_id) REFERENCES Customers(cust_id)
);
""")

# ---------------------------
# Transactions
# ---------------------------
# Note: store dates as TEXT in ISO format 'YYYY-MM-DD' (common practice in SQLite)
cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions (
    trans_id   INTEGER PRIMARY KEY,
    acc_id     INTEGER NOT NULL,
    trans_type TEXT    NOT NULL CHECK (trans_type IN ('deposit','withdrawal')),
    amount     REAL    NOT NULL CHECK (amount >= 0.0),
    date       TEXT    NOT NULL,  -- ISO 'YYYY-MM-DD'
    FOREIGN KEY (acc_id) REFERENCES Accounts(acc_id)
);
""")

# Persist changes and close
conn.commit()
conn.close()
