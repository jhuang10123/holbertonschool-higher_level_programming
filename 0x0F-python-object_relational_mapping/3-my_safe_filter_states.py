#!/usr/bin/python3
"""
lists states from the database hbtn_0e_0_usa w/ name
matching input. safe from MySQL injections
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row == argv[4]:
            print(row)
    cur.close()
    db.close()
