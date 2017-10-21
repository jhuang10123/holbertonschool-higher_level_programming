#!/usr/bin/python3
"""
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
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

    obj = session.query(State).filter(State.name.like("%a%")).all()
    for elem in obj:
        session.delete(elem)
    session.commit()
    session.close()
