class BankAccount:
    def __init__(self, candidate_name,account_number, balance):
        self.candidate_name = candidate_name
        self.account_number = account_number
        self.balance = balance
    def insufficient_balance(self):
        return f"insufficient balance in account {self.account_number}"
        
    def deposit(self, amount):
        if amount<= 0:
            return "Invalid deposit amount"
        self.balance += amount
        return f"Dposit successful. Available balance {self.balance}"
    def withdraw(self, amount):
        if amount<=0:
            return ("Insufficient funds")
        if self.balance<=0 or amount>self.balance:
            return self.insufficient_balance()
        self.balance -= amount
        
        return(
            f"Transaction successful\n." 
             
            f"Candidate Name: {self.candidate_name}", 
            f"Account No.: {self.account_number}", 
            f"Remaining balance: {self.balance}"
        )
