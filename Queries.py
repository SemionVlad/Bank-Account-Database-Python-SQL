"""
Queries.py
- Simple reporting helpers that print table contents to stdout.
- Each function opens its own connection to keep usage explicit and simple.
- SQL kept straightforward (SELECTs with JOIN where needed).
"""

import sqlite3

def show_customers():
    """
    Print all rows from the Customers table.

    Side effects:
        Prints each row tuple returned by: SELECT * FROM Customers
    Returns:
        None
    """
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    result = cursor.execute('SELECT * FROM Customers')
    for row in result:
        print(row)
    conn.close()


def show_accounts():
    """
    Print account details joined with the owning customer's name.

    Query:
        SELECT Accounts.acc_id, Customers.name, Accounts.acc_type, Accounts.balance
        FROM Accounts JOIN Customers ON Accounts.cust_id = Customers.cust_id
    Side effects:
        Prints each joined row tuple.
    Returns:
        None
    """
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    result = cursor.execute('''
            SELECT Accounts.acc_id, Customers.name, 
                   Accounts.acc_type, Accounts.balance 
            FROM Accounts JOIN Customers ON 
                 Accounts.cust_id = Customers.cust_id ''')
    for row in result:
        print(row)
    conn.close()


def show_transactions():
    """
    Print all rows from the Transactions table.

    Side effects:
        Prints each row tuple returned by: SELECT * FROM Transactions
    Returns:
        None
    """
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM Transactions")
    for row in result:
        print(row)
    conn.close()


if __name__ == '__main__':
    print('\n\nCustomers')
    show_customers()
    print('\n\nAccounts')
    show_accounts()
    print('\n\nTransactions')
    show_transactions()
