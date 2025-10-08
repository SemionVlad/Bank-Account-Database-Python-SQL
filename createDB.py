"""
createDB.py
- Opens/creates 'bank.db' and defines the schema.
- Tables: Customers, Accounts, Transactions.
- Keeps the SQL simple (sqlite3 stdlib, execute calls).
"""

import sqlite3

# Connect to the SQLite DB file (created if not exists)
conn = sqlite3.connect('bank.db')

# Enforce FOREIGN KEY constraints for this connection
conn.execute("PRAGMA foreign_keys = ON;")

cursor = conn.cursor()

# ------------------------------------------------------------------
# Customers - Connect to the SQLite DB file (created if not exists)
# ------------------------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    cust_id INTEGER PRIMARY KEY,
    name    TEXT    NOT NULL,
    address TEXT,
    email   TEXT    UNIQUE
);
""")

# ------------------------------------------------------------------
# Accounts - Connect to the SQLite DB file (created if not exists)
# (Minimal checks to demonstrate constraints.)
# ------------------------------------------------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Accounts (
    acc_id   INTEGER PRIMARY KEY,
    cust_id  INTEGER NOT NULL,
    acc_type TEXT    NOT NULL CHECK (acc_type IN ('Savings','Checking')),
    balance  REAL    NOT NULL DEFAULT 0.0,
    FOREIGN KEY (cust_id) REFERENCES Customers(cust_id)
);
""")

# ------------------------------------------------------------------
# Transactions - deposits/withdrawals for an account.
# Store dates as ISO text 'YYYY-MM-DD' (common for SQLite).
# ------------------------------------------------------------------
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
