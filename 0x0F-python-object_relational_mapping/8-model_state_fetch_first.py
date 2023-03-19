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
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                        argv[2],
                                                        argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
