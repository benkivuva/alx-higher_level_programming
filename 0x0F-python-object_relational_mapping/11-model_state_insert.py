#!/usr/bin/python3

"""
script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa via SQLAlchemy
"""

from sys import argv
from model_state import Base, State  # Import the State class and Base instance
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Set up the database connection using command line arguments
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create a session using the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Query and print the newly added state's id
    for instance in session.query(State).filter(State.name == "Louisiana"):
        print("{}".format(instance.id))

    # Close the session
    session.close()
