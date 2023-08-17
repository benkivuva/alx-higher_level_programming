#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]

    # Connect to the MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute queries
    cur = conn.cursor()

    # Execute the SELECT query to retrieve states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
