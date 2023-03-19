#!/usr/bin/python3
"""
script that list all states from the database hbtn_0e_0_usa

it takes in three arguments:
mysql username, mysql password, and database name

get the mysql username, password, and database name from command line arguments
connect to the MySQL server
prepare a cursor object using cursor() method
execute SQL query to select all states from the database
fetch all the rows using fetchall() method
print the results
disconnect from server
"""
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """state representation"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
