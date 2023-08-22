# creating new database connections.
# defining columns in a database table and their types.
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey 
# to create new Session objects, to interact with the database.
# relationships between tables (like foreign keys).
from sqlalchemy.orm import sessionmaker, relationship
# used to create a new base class for declarative models.
from sqlalchemy.ext.declarative import declarative_base
#  ensures that only valid dates get stored 
from sqlalchemy import Date

engine=create_engine('sqlite:///expenses.db')# connection to SQLite

Base = declarative_base() # base class that other data models will inherit 

class User(Base): # represents users of the system 
    __tablename__='users'#naming of the database table 
    # each colunm type can hold a type of data
    id=Column(Integer, primary_key=True)
    username=Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    # establishes a two way relationship between User and Expense 
    expenses=relationship('Expense', back_populates='user')

class Expense(Base): # represents the expenses of the system 
    __tablename__='expenses'
    
    id=Column(Integer, primary_key=True)
    category =Column(String, nullable=False)
    amount=Column(Float, nullable=False)
    date=Column(Date, nullable=False)
    user_id=Column(Integer, ForeignKey('users.id')) # many-to-one relationship between expense & user 
    # one user can have many expenses, but each expense belongs to one user.

    user=relationship('User', back_populates='expenses') # establishes a two way relationship between User and Expense

# instructing SQLAlchemy to create the tables in the database if they don't exist. 
Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine) # creates new database session objects. session is bound to SQLite
session=Session() # instance of the session to interact with the database 