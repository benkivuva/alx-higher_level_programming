#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
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

    # Execute the query to select all cities
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cur.execute(query)

    # Fetch and display the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
