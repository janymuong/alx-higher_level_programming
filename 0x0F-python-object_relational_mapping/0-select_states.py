#!/usr/bin/python3
'''
module:
script that lists all states from the database `hbtn_0e_0_usa`.
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

    # retrieve states
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    # get connection variables from command-line arguments:
    db_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_states(db_user, password, db_name)
