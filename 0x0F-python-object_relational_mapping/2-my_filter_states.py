#!/usr/bin/python3

"""
Print database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access the database and print states
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BY state.id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
