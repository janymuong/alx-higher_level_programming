#!/usr/bin/python3
'''
module ORM: SQLAlchmey
delete a state object from db hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':

    # connection variables from command-line arguments
    db_user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # create the engine - connection to the database
    engine = create_engine(
        f'mysql+mysqldb://{db_user}:{passwd}@localhost:3306/{db_name}'
        )

    Session = sessionmaker(bind=engine)
    session = Session()

    # update a new State object
    states = session.query(State).order_by(State.id).filter(
        State.name.ilike(f'%a%')).all()

    for state in states:
        session.delete(state)

    # persist session to db;
    session.commit()

    session.close()
