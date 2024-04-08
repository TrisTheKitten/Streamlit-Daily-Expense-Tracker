import matplotlib.pyplot as plt
from reports import generate_income_report, generate_expense_report

def create_income_pie_chart():
    income_data = generate_income_report()
    categories = [data[0] for data in income_data]
    amounts = [data[1] for data in income_data]

    fig, ax = plt.subplots()
    ax.pie(amounts, labels=categories, autopct='%1.1f%%')
    ax.set_title("Income Distribution")
    return fig

def create_expense_pie_chart():
    expense_data = generate_expense_report()
    categories = [data[0] for data in expense_data]
    amounts = [data[1] for data in expense_data]

    fig, ax = plt.subplots()
    ax.pie(amounts, labels=categories, autopct='%1.1f%%')
    ax.set_title("Expense Distribution")
    return fig