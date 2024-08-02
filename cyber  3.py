import tkinter as tk
import sqlite3

def create_database():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            amount REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense(name, amount):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (name, amount) VALUES (?, ?)
    ''', (name, amount))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    rows = cursor.fetchall()
    conn.close()
    return rows

def submit_expense():
    name = entry_name.get()
    amount = entry_amount.get()
    add_expense(name, float(amount))
    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)

create_database()

root = tk.Tk()
root.title("Expense Sharing")

tk.Label(root, text="Name:").grid(row=0)
tk.Label(root, text="Amount:").grid(row=1)

entry_name = tk.Entry(root)
entry_amount = tk.Entry(root)

entry_name.grid(row=0, column=1)
entry_amount.grid(row=1, column=1)

tk.Button(root, text="Add Expense", command=submit_expense).grid(row=2, column=0)
tk.Button(root, text="View Expenses", command=lambda: print(view_expenses())).grid(row=2, column=1)

root.mainloop()
