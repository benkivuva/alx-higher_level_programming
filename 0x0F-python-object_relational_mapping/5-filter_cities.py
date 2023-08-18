#!/usr/bin/python3

"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database, state_name = argv[1], argv[2], argv[3], argv[4]

    #Connect to Mysql server
    conn = MySQLdb.connect(
            host = "localhost",
            port = 3306,
            user = username,
            passwd = password,
            db = database
    )

    # Create cursor to execute the queries
    cur = conn.cursor()

    #execute the query
    query = "SELECT cities.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))

    # fetch and display the results
    city_names = [row[0] for row in cur.fetchall()]
    for city_name in city_names:
        print(city_name)

    cur.close()
    conn.close()
