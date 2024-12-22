#!/usr/bin/python3
"""Displays all values in the cities table where name matches query"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_host = 'localhost'
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_state_name = argv[4]
    db_port = 3306

    db_connection = MySQLdb.connect(host=db_host,
                                    user=db_user,
                                    passwd=db_passwd,
                                    db=db_name,
                                    port=db_port
                                    )

    query = """
                SELECT cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;
            """

    db_cursor = db_connection.cursor()
    db_cursor.execute(query, (db_state_name,))
    cities = [city for obj in list(db_cursor) for city in obj]

    print(", ".join(cities))

    db_cursor.close()
    db_connection.close()
