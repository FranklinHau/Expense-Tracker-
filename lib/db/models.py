# creating new database connections.
# defining columns in a database table and their types.
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey 
# to create new Session objects, to interact with the database.
# relationships between tables (like foreign keys).
from sqlalchemychemy.orm import sessionmaker, relationship
# used to create a new base class for declarative models.
from aqlalchemychemy.ext.declarative import declarative_base

Base = declarative_base() #base class that other data models will inherit 

class User(Base): #represents users of the system 
    __tablename__='users'#naming of the database table 
    #each colunm type can hold a type of data
    id=Column(Integer, primary_key=True)
    username=Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    #establishes a two way relationship between User and Expense 
    expenses=relationship('Expense', back_populates='user')

class Expense(Base):
    __tablename__='expenses'
    
    id=Column(Integer, primary_key=True)
    category =Column(String, nullable=False)
    amount=Column(Float, nullable=False)
    date=Column(String, nullable=False)
    user_id=Column(Integer, ForeignKey('users.id'))

    