#!/usr/bin/python3
"""Lists all states from a database"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    if (len(argv) != 4):
        print("[Usage]: {} <mysql username> <mysql password> \
<mysql database name>".format(argv[0])
              )
        exit(1)

    db_host = 'localhost'
    db_username = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_port = 3306

    db_connection = MySQLdb.connect(host=db_host,
                                    user=db_username,
                                    passwd=db_passwd,
                                    db=db_name,
                                    port=db_port
                                    )

    query = """
                SELECT *
                FROM states
                ORDER BY states.id ASC
            """

    db_cursor = db_connection.cursor()
    db_cursor.execute(query)

    for state in db_cursor:
        print(state)

    db_cursor.close()
    db_connection.close()
