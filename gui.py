import streamlit as st
from main import add_income, add_expense, clear_all_data
from reports import generate_income_report, generate_expense_report
from visualizations import create_income_pie_chart, create_expense_pie_chart
from database import Session, create_tables
from models import Income, Expense
from sqlalchemy import func

def main():
    create_tables()
    st.set_page_config(page_title="Expense Tracker", page_icon=":money_with_wings:", layout="wide")
    
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
            body {
                font-family: 'Montserrat', sans-serif;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("Personal Expense Tracker")
    
    menu = ["Add Income", "Add Expense", "Check Balance", "Visualizations", "Clear Data"]
    choice = st.sidebar.selectbox("Select an option", menu)
    
    if choice == "Add Income":
        st.subheader("Add Income")
        with st.form(key="income_form"):
            amount = st.number_input("Enter the amount", min_value=0.0, step=0.01)
            category = st.text_input("Enter the category")
            submitted = st.form_submit_button("Add Income")
            if submitted:
                add_income(amount, category)
                st.success(f"Income of {amount} added to category '{category}'.")
    
    elif choice == "Add Expense":
        st.subheader("Add Expense")
        with st.form(key="expense_form"):
            amount = st.number_input("Enter the amount", min_value=0.0, step=0.01)
            category = st.text_input("Enter the category")
            submitted = st.form_submit_button("Add Expense")
            if submitted:
                add_expense(amount, category)
                st.success(f"Expense of {amount} added to category '{category}'.")
    
    elif choice == "Check Balance":
        st.subheader("Current Balance")
        session = Session()
        total_income = session.query(func.sum(Income.amount)).scalar() or 0
        total_expense = session.query(func.sum(Expense.amount)).scalar() or 0
        balance = total_income - total_expense

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Balance", f"฿{balance:.2f}")
            
        with col2:
            st.metric("Income", f"฿{total_income:.2f}")
            st.metric("Expense", f"฿{total_expense:.2f}")

        st.subheader("Recent Transactions")
        sort_options = ["Most to Least", "Least to Most", "Recent to Oldest", "Oldest to Recent"]
        selected_sort = st.selectbox("Sort by", sort_options)

        if selected_sort == "Most to Least":
            incomes = session.query(Income).order_by(Income.amount.desc()).limit(5)
            expenses = session.query(Expense).order_by(Expense.amount.desc()).limit(5)
        elif selected_sort == "Least to Most":
            incomes = session.query(Income).order_by(Income.amount.asc()).limit(5)
            expenses = session.query(Expense).order_by(Expense.amount.asc()).limit(5)
        elif selected_sort == "Recent to Oldest":
            incomes = session.query(Income).order_by(Income.date.desc()).limit(5)
            expenses = session.query(Expense).order_by(Expense.date.desc()).limit(5)
        else: 
            incomes = session.query(Income).order_by(Income.date.asc()).limit(5)
            expenses = session.query(Expense).order_by(Expense.date.asc()).limit(5)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Incomes")
            for income in incomes:
                st.write(f"+ ฿{income.amount:.2f}")
                st.write(f"{income.category.name}, on {income.date}")
                st.write("---")

        with col2:
            st.subheader("Expenses")
            for expense in expenses:
                st.write(f"- ฿{expense.amount:.2f}")
                st.write(f"{expense.category.name}, on {expense.date}")
                st.write("---")
    
    elif choice == "Visualizations":
        st.subheader("Income and Expense Visualizations")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Income Distribution")
            income_fig = create_income_pie_chart()
            st.pyplot(income_fig)
        with col2:
            st.subheader("Expense Distribution")
            expense_fig = create_expense_pie_chart()
            st.pyplot(expense_fig)
    
    elif choice == "Clear Data":
        st.subheader("Clear Data")
        if st.button("Clear All Data"):
            clear_all_data()
            st.success("All data cleared successfully.")

if __name__ == '__main__':
    main()