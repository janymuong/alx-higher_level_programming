#!/usr/bin/python3
'''
script: 101-relationship_states_cities_list.py
lists all State objects and corresponding City objects
in the database hbtn_0e_101_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # connection variables from command-line arguments
    db_user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # create the engine - connection to the database
    engine = create_engine(
        f'mysql+mysqldb://{db_user}:{passwd}@localhost:3306/{db_name}'
        )

    # creating a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # select all State objects with their corresponding City objects
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'\t{city.id}: {city.name}')
