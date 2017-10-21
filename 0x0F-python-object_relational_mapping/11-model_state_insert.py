#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



ce = ('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                       argv[2],
                                                       argv[3]))
engine = create_engine(ce)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new = State(name="Louisiana")
session.add(new)

new = session.query(State).filter_by(State.name == "Louisiana").first()
print(new.id)

session.commit()
session.close()
