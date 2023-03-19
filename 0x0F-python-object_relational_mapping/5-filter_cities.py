#!/usr/bin/python3
"""
script that list all states that contain the search name
from the database hbtn_0e_0_usa

it takes in four arguments:
mysql username, mysql password, database name and a search name

get the mysql username, password, and database name from command line arguments
connect to the MySQL server
prepare a cursor object using cursor() method
execute SQL query to select all states from the database
fetch all the rows using fetchall() method
print the results if only the state is equal to the search name
disconnect from server
"""

import MySQLdb
import sys
from sys import argv

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost", port=3306, user=mysql_user,
            passwd=mysql_password, db=database_name)

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))

    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))
    db.close()
