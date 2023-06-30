#!/usr/bin/python3
'''
SQLAlchemy
module: 14-model_city_fetch_by_state
prints all City objects from the database hbtn_0e_14_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # select all City objects from the database
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter_by(
            id=city.state_id).first().name
        print(f'{state_name}: ({city.id}) {city.name}')
