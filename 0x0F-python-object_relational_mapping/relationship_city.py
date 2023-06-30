#!/usr/bin/python3
'''
module ORM: SQLAlchemy
model City: link class to table in database
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    '''City:
    class representing the cities table in db;
    subclasses Base()
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
