#!/usr/bin/python3
"""Creates State "California" with city "San Francisco"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


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

    state = State(name="California")
    city = City(name="San Francisco", state=state)

    session.add(state)
    session.add(city)
    session.commit()

    session.close()
