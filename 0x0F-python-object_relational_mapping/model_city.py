#!/usr/bin/python3
"""Contains the City class definition and an instance of \
Base = declarative_base()"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class definition"""

    __tablename__ = "cities"

    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True
                )

    name = Column(String(128),
                  nullable=False
                  )

    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False
                      )
