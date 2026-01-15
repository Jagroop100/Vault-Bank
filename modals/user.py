import json
import sqlite3
from modals.expenses import expense
from modals.database import connect_db
from modals.expenses import expense, CardExpense, CashExpense
class User:
    def __init__(self, candidate_name,account):
        self.candidate_name = candidate_name
        self.account=account
        self.session_expenses=[]
    def new_expense(self,expense):
        if expense.amount >self.account.balance:
            print("Insufficient Balance. Remaining Balance: {self.balance}")
            return False
        self.session_expenses.append(expense)
        return True
    def total_expense(self):
        return sum(e.amount for e in self.session_expenses)
    def load_expenses(self):
        loaded_data = []
        for exp in loaded_data:
            self.session_expenses.append(exp)
    
    def save_expenses(self,filename="expenses.json"):
        with open(filename, "w")as f:
            json.dump(
                [e.to_dict() for e in self.session_expenses],
                f,
                indent = 4
            )
    def load_expenses (self, filename="expenses.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for e in data:
                payment_method=e.get("payment_method", "Cash")
                if payment_method == "Card":
                    exp=CardExpense(e["amount"], e["category"], e["date"], e["time"])
                else:
                    exp=CashExpense(e["amount"], e["category"], e["date"], e["time"])
                
                self.session_expenses.append(exp)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
            
    def save_expense_to_db(self,exp):
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO expenses (amount, category, date, time, payment_type)
        VALUES (?, ?, ?, ?, ?)
    """, (exp.amount, exp.category, exp.date, exp.time, exp.payment_method))
        conn.commit()
        conn.close()
    def get_transaction_history(self):
        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor ()
        cur.execute("SELECT date, time, category,amount,payment_type FROM expenses")
        rows = cur.fetchall()
        conn.close()
        return rows
import json

def save_expenses(self):
    with open("expenses.json", "w") as f:
        json.dump([e.to_dict() for e in self.session_expenses], f, indent=4)

def load_expenses(self):
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
            for e in data:
                self.session_expenses.append(expense.from_dict(e))
    except FileNotFoundError:
        pass