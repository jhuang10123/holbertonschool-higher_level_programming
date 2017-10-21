#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    ce = ('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                           argv[2],
                                                           argv[3]))
    engine = create_engine(ce)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state_id, city.id, city.name))
    session.close()
