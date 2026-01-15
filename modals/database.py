import sqlite3
def connect_db():
    return sqlite3.connect("expenses.db")
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            date TEXT,
            time TEXT,
            payment_type TEXT,
            type TEXT
        )
    """)
def clear_transactions():
    conn = connect_db
    cur = conn.cursor()
    cur.execute("DELETE from expenses")
    conn.commit()
    conn.close()