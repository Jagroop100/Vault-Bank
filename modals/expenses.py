class expense:
    def __init__(self, amount, category, date,time):
        self.amount = amount
        self.category = category
        self.date= date
        self.time= time
    @property
    def payment_method(self):
        return self.__class__.__name__.replace("Expense", "")
    def to_dict(self):
        return{
            "amount": self.amount,
            "category": self.category,
            "date":self.date,
            "time": self.time
        }
    @staticmethod
    def from_dict(data):
        return expense(
            data["amount"],
            data["category"],
            data["date"],
            data["time"]
        )
    def __str__(self):
        return f"{self.category} | ₹{self.amount} | {self.date} {self.time} | {self.__class__.__name__}"
        
    def process_payment(self):
        raise NotImplementedError("Subclasses must implement this")
class CardExpense(expense):
    def process_payment(self):
        return ("Payment successful with card")
class CashExpense(expense):
    def process_payment(self):
        return ("Payment successful with cash")      