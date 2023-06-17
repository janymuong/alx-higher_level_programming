#!/usr/bin/python3
'''
module ORM: SQLAlchmey
prints states with char: 'a' in name
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

    # select states that have char 'a' in name
    states = session.query(State).order_by(State.id).filter(
        State.name.ilike(f'%a%')).all()

    for state in states:
        print(f'{state.id}: {state.name}')
