#!/usr/bin/python3
"""Lists all State objects"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_host = "localhost"
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_port = 3306

    db_url = "mysql+mysqldb://{}:{}@{}:{}/{}".format(db_user,
                                                     db_passwd,
                                                     db_host,
                                                     db_port,
                                                     db_name
                                                     )

    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
