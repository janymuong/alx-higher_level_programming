#!/usr/bin/python3
'''
module ORM: SQLAlchmey
link class to table in database
'''

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(sys.argv[1], sys.argv[2], sys.argv[3]))

# declarative_base() function sets up the necessary Base for mapping
Base = declarative_base()


class State(Base):
    '''State:
    class representing the states table in db;
    subclasses Base()
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == '__main__':
    # creating the database tables based on the SQLAlchemy model
    Base.metadata.create_all(engine)
