import streamlit as st
from modals.bank import BankAccount
from modals.expenses import CardExpense, CashExpense
from modals.user import User
from modals.database import create_table
from datetime import datetime
st.set_page_config(page_title="Expense Tracker", layout="centered")
create_table()
if "user" not in st.session_state:
    account = BankAccount("Tom", "DE5089787998678700", 2004)
    user = User("Tom", account)
    user.load_expenses()
    st.session_state.user = user
user = st.session_state.user

st.title("Expense Tracker")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Card Expense",
        "Add Cash Expense",
        "View Expenses",
        "Transaction History",
        "Total Expense",
    ],
)

if menu == "Add Card Expense":
    st.subheader("Add Card Expense")

    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    category = st.text_input("Category")

    if st.button("Add Card Expense"):
        now = datetime.now()
        expense = CardExpense(
            amount,
            category,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
        )

        if user.new_expense(expense):
            st.success(expense.process_payment())
            user.save_expense_to_db(expense)
            user.save_expenses()
        else:
            st.error("Insufficient balance")

elif menu == "Add Cash Expense":
    st.subheader("Add Cash Expense")

    amount = st.number_input("Amount", min_value=0.0, step=1.0)
    category = st.text_input("Category")

    if st.button("Add Cash Expense"):
        now = datetime.now()
        expense = CashExpense(
            amount,
            category,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
        )

        if user.new_expense(expense):
            st.success(expense.process_payment())
            user.save_expense_to_db(expense)
            user.save_expenses()
        else:
            st.error("Insufficient balance")
elif menu == "View Expenses":
    st.subheader("Expenses")

    if not user.session_expenses:
        st.info("No expenses recorded yet.")
    else:
        for exp in user.session_expenses:
            st.write(exp)

elif menu == "Transaction History":
    st.subheader("Transaction History")

    history = user.get_transaction_history()

    if not history:
        st.info("No transactions found.")
    else:
        for t in history:
            st.write(f"{t[0]} {t[1]} | {t[2]} ${t[3]} | {t[4]}")
            
elif menu == "Total Expense":
    st.subheader("Total Expense")
    st.metric("Total Spent", f"${user.total_expense()}")
