#!/usr/bin/python3
'''
module:
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
MySQLdb (safe from MySQL injection)
'''

import MySQLdb
import sys


def safe_filter(db_user, password, db_name, state_name):
    '''connect to the MySQL server,
    retrieve and print the values in the states table
    where name matches the provided argument.
    '''
    db = MySQLdb.connect(host='localhost', port=3306, user=db_user,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    # SQL - injection safe expression
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # retrieve and print the matching states
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    # get connection variables and state name from command-line arguments
    db_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    safe_filter(db_user, password, db_name, state_name)
