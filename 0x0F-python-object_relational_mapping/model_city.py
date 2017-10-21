#!/usr/bin/python3
"""
contains the class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship

class City(Base):
    """ class inherited from Base """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)

