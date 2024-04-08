from database import Session, clear_data
from models import Income, Expense, Category

def add_income(amount, category_name):
    session = Session()
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
    income = Income(amount=amount, category=category)
    session.add(income)
    session.commit()

def add_expense(amount, category_name):
    session = Session()
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
    expense = Expense(amount=amount, category=category)
    session.add(expense)
    session.commit()

def clear_all_data():
    clear_data()