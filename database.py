from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

db_file = "expense_tracker.db"
engine = create_engine(f'sqlite:///{db_file}')
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def clear_data():
    Base.metadata.drop_all(engine)
    create_tables()