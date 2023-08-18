#!/usr/bin/python3
"""
script that prints the first State object from the database hbtn_0e_6_usa
via SQLAlchemy
"""
if __name__ == "__main__":

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        instance = session.query(State).first()
        print("{}: {}".format(instance.id, instance.name))
    except:
        print("Nothing")
    session.close()
