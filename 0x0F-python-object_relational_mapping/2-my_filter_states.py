#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database, search_name = argv[1], argv[2], argv[3], argv[4]

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

    # Construct the SQL query
    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC").format(search_name)
    cur.execute(query)

    # Fetch and display the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()
