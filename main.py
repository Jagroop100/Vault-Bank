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
        return "payment success"
class category:
    def __init__(self,name):
        self.name = name
class user:
    def __init__(self, username):
        self.username = username
        self.expense = []
    def new_expense(self,expense):
        self.expense.append(expense)
    def total_expense(self):
        return sum(expense in self.expense)
        
