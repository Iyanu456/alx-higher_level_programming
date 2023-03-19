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
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    data = session.query(State).order_by(State.id)\
                               .filter(State.name.like("%a%")).all()
    for row in data:
        print("{}: {}".format(row.id, row.name))
    session.close()
