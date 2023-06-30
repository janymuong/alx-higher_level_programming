#!/usr/bin/python3
'''
module ORM: SQLAlchmey
lists all State objects from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # select all State objects(query objects) and sort them by id
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f'{state.id}: {state.name}')
