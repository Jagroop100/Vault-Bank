import json
class BankAccount:
    def __init__(self, candidate_name,account_number, balance):
        self.candidate_name = candidate_name
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
def load_account_details(filename = "balance.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data
def save_account_data(data, filename = "balance.json"):
    with open("balance.json","w") as f:
        json.dump(data, f, indent=4)