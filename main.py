import json
from modals.bank import BankAccount
from modals.expense import expense, cardExpense, category
from modals.user import user

if __name__ == "__main__":
    u = user("Alice")
    food = category("Pringles")

    e = cardExpense(200, food.name, "2025-12-22", "23:45", "Card")
    e.process_payment()

    u.new_expense(e)

    print(e)
    print("Total expense:", u.total_expense())

    acc = BankAccount("Alice", "001", 1000)
    acc.withdraw(300)
    acc.deposit(100)
    print("Final balance:", acc.balance)