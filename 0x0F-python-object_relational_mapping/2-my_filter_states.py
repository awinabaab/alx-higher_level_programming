#!/usr/bin/python3
"""Displays all values in the states table where name matches query"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_host = 'localhost'
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_queryfilter = argv[4]
    db_port = 3306

    db_connection = MySQLdb.connect(host=db_host,
                                    user=db_user,
                                    passwd=db_passwd,
                                    db=db_name,
                                    port=db_port
                                    )

    query = """
                SELECT *
                FROM states
                WHERE states.name = BINARY '{}'
                ORDER BY states.id ASC;
            """

    db_cursor = db_connection.cursor()
    db_cursor.execute(query.format(db_queryfilter))

    for state in db_cursor:
        print(state)

    db_cursor.close()
    db_connection.close()
