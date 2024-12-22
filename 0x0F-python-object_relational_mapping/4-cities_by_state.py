#!/usr/bin/python3
"""Lists all cities from the hbtn_0e_4_usa"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_host = 'localhost'
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_port = 3306

    db_connection = MySQLdb.connect(host=db_host,
                                    user=db_user,
                                    passwd=db_passwd,
                                    db=db_name,
                                    port=db_port
                                    )

    query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC
            """
    db_cursor = db_connection.cursor()
    db_cursor.execute(query)

    for city in db_cursor:
        print(city)

    db_cursor.close()
    db_connection.close()
