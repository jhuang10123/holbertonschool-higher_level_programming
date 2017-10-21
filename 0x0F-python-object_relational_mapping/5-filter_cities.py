#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.id, cities.name FROM cities \
    JOIN states ON cities.state_id=states.id WHERE states.name \
    like '{}' ORDER BY cities.id ASC".format(argv[4]))

    query_rows = cur.fetchall()
    ct = []
    for row in query_rows:
        ct.append(row[1])
    for each in ct:
        print("{}".format(each), end=", ")

    cur.close()
    db.close()
