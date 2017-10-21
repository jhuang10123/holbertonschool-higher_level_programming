#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
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

    update = session.query(State).filter_by(id=2).first()
    update.name = "New Mexico"
    session.commit()
    session.close()
