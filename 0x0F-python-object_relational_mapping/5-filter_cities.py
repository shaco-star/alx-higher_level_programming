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
    cur.execute("""SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %s
            ORDER BY cities.id ASC""", (argv[4],))
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join(row[1] for row in rows))
    cur.close()
    db.close()
