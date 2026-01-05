class expense:
    def __init__(self, amount, category, date,time,payment_method):
        self.amount = amount
        self.category = category
        self.date= date
        self.time= time
        self.payment_method = payment_method
    def __str__(self):
        return f"{self.date}, {self.time}| {self.category}|{self.amount}| {self.payment_method}"
class cardExpense(expense):
    def process_payment(self):
        print("payment successful")
class category:
    def __init__(self, name):
        self.name = name