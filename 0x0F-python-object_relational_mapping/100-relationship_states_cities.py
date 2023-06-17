#!/usr/bin/python3
'''
script: 100-relationship_states_cities.py
creates the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa
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

    # create all tables in the database - db.create_all()
    Base.metadata.create_all(engine)

    # create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # create the objects: State "California" and the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    california.cities.append(san_francisco)

    # ommit session/changes to the database
    session.add(california)
    session.add(san_francisco)
    session.commit()
    session.close()
