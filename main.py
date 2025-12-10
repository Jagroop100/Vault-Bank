import json
class expense:
    def __init__(self, amount, category, date,time,payment_method):
        self.amount = amount
        self.category = category
        self.date= date
        self.time= time
        self.payment_method = payment_method
    def __str__(self):
        pass
class cardexpense(expense):
    def payment_method(self):
        return "transaction successful"
class category:
    def __init__(self,name):
        self.name = name
class user:
    def __init__(self, candidate_name):
        self.candidate_name = candidate_name
        self.expense = []
    def new_expense(self,expense):
        self.expense.append(expense)
    def total_expense(self):
        return sum(expense in self.expense)
    
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient funds")
        self.balance -= amount
def load_account_details():
    with open("balance.json") as f:
        return
def save_account_data(data):
    with open("balance.json","w") as f:
        json.dump(data,f, indent=4)
        