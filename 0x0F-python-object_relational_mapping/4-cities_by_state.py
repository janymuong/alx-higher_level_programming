#!/usr/bin/python3
'''
module:
script that lists all cities from the database hbtn_0e_4_usa.
MySQLdb
'''

import MySQLdb
import sys


def list_cities(db_user, password, db_name):
    '''connect to the MySQL server;
    retrieve and print all cities from the database.
    '''
    db = MySQLdb.connect(host='localhost', port=3306, user=db_user,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    # retrieve all cities with their associated states
    cursor.execute(
        '''
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        ''')
    cities = cursor.fetchall()

    # print cities with their associated state
    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == '__main__':
    # get connection variables from command-line arguments
    db_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_cities(db_user, password, db_name)
