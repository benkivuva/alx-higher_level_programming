#!/usr/bin/python3

"""
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa via SQLAlchemy
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a connection to the MySQL server
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost/{database}')

    # Bind the engine to the Base class
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and delete State objects with a name containing the letter 'a'
    states_to_delete = session.query(
            State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
