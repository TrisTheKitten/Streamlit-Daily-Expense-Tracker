from database import Session
from models import Income, Expense, Category
from sqlalchemy import func

def generate_income_report():
    session = Session()
    income_report = session.query(Category.name, func.sum(Income.amount)).join(Income).group_by(Category.name).all()
    return income_report

def generate_expense_report():
    session = Session()
    expense_report = session.query(Category.name, func.sum(Expense.amount)).join(Expense).group_by(Category.name).all()
    return expense_report