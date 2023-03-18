#!/usr/bin/python3
import MySQLdb
import sys

"""
    get the mysql username, password, and database name from command line arguments
    connect to the MySQL server
    prepare a cursor object using cursor() method
    execute SQL query to select all states from the database
    fetch all the rows using fetchall() method
    print the results
    disconnect from server
"""
mysql_user = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)
cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

rows = cursor.fetchall()

for row in rows:
    print(row)

db.close()

