# creating new database connections.
# defining columns in a database table and their types.
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey 
# to create new Session objects, to interact with the database.
# relationships between tables (like foreign keys).
from sqlalchemychemy.orm import sessionmaker, relationship
# used to create a new base class for declarative models.
from aqlalchemychemy.ext.declarative import declarative_base