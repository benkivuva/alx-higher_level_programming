#!/usr/bin/python3
"""
Safe script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv


def main():
    # Extract command line arguments
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

    # Create the SQL query with user input using parameterized query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (search_name,))

    # Fetch and display the results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
