from modals.bank import BankAccount
from modals.expenses import expense, CardExpense, CashExpense
from modals.user import User
from modals.database import create_table
from datetime import datetime
def show_menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Card Expense")
    print("2. Add Cash Expense")
    print("3. View Expenses")
    print("4. View Transaction History")
    print("5. View Total Expense")
    print("0. Exit")


def main():
    create_table()

    account = BankAccount("Tom", "DE5089787998678700", 2004)
    user = User("Tom", account)
    user.load_expenses()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1" or choice == "2":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")

            now = datetime.now()
            date = now.strftime("%Y-%m-%d")
            time = now.strftime("%H:%M:%S")

            if choice == "1":
                expense = CardExpense(amount, category, date, time)
            else:
                expense = CashExpense(amount, category, date, time)

            if user.new_expense(expense):
                print(expense.process_payment())
                user.save_expense_to_db(expense)
                user.save_expenses()
            else:
                print("Insufficient balance.")

        elif choice == "3":
            print("\n--- Expenses ---")
            for exp in user.session_expenses:
                print(exp)

        elif choice == "4":
            print("\n--- Transaction History ---")
            for t in user.get_transaction_history():
                print(f"{t[0]} {t[1]} | {t[2]} ${t[3]} | {t[4]}")

        elif choice == "5":
            print("Total Expense:", user.total_expense())

        elif choice == "0":
            print("Exiting Expense Tracker...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()