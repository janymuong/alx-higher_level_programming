#!/usr/bin/python3
'''
module:
script that lists states with N from the database `hbtn_0e_0_usa`.
MySQLdb
'''

import MySQLdb
import sys


def list_states(db_user, password, db_name):
    '''connect to the MySQL server:
    retrieve and print the list of states from the database.
    '''
    db = MySQLdb.connect(host='localhost', port=3306, user=db_user,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    # retrieve states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'"
                   "ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    # get connection variables from command-line arguments:
    db_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(db_user, password, db_name)
