#!/usr/bin/python3
'''
module:
script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
MySQLdb
'''

import MySQLdb
import sys


def filter_cities(db_user, password, db_name, state_name):
    '''connect to the MySQL server, retrieve and print
    all cities of the specified state.
    '''
    db = MySQLdb.connect(host='localhost', port=3306, user=db_user,
                         passwd=password, db=db_name)
    cursor = db.cursor()

    # retrieve cities of the specified state
    query = (
        '''
        SELECT cities.name FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name LIKE BINARY %s
        ORDER BY cities.id ASC
        ''')
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    # check if cities exists; print them
    if cities:
        city_names = [city[0] for city in cities]
        print(', '.join(city_names))
    else:
        print()

    cursor.close()
    db.close()


if __name__ == '__main__':
    # get connection variables and state name from command-line arguments
    db_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(db_user, password, db_name, state_name)
