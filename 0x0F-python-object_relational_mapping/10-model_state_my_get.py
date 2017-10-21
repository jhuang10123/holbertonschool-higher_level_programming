#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    ce = ('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                           argv[2],
                                                           argv[3]))
    engine = create_engine(ce)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    sess = session.query(State).filter(State.name == argv[4]).all()
    for elem in sess:
        if elem is None:
            print("Not found")
        else:
            print("{:d}".format(elem.id))

        session.close()
