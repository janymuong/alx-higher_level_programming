#!/usr/bin/python3
'''module:
102-relationship_cities_states_list
lists all City objects from the database hbtn_0e_101_usa
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

    # create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # select all City objects with their associated State objects
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name
        print(f'{city.id}: {city.name} -> {state_name}')
