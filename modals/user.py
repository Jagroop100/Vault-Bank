class user:
    def __init__(self, candidate_name):
        self.candidate_name = candidate_name
        self.expenses = []
    def new_expense(self,expense):
        self.expenses.append(expense)
    def total_expense(self):
        return sum(m.amount for m in self.expenses)