#!/usr/bin/python3
'''
module:
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.
MySQLdb
'''

import MySQLdb
import sys


def filter_states(db_user, password, db_name, state_name):
    '''Connect to the MySQL server
    retrieve and print the values in the states table
    where name matches the provided argument.
    '''
    db = MySQLdb.connect(host='localhost', port=3306, user=db_user,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    # create the SQL query object with user input
    # Retrieve and print the matching states
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   "ORDER BY id ASC".format(state_name))
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

    filter_states(db_user, password, db_name, state_name)
