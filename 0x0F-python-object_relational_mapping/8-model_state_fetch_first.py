#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_sess = session.query(State).first()

    if first_sess == None:
        print("Nothing")
    else:
        print("{}: {}".format(first_sess.id, first_sess.name))
    session.close()
