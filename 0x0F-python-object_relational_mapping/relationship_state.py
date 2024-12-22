#!/usr/bin/python3
"""Contains the State class definition and an instance of \
Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class definition"""

    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
                nullable=False
                )

    name = Column(String(128),
                  nullable=False
                  )

    cities = relationship("City",
                          backref="state",
                          cascade="all, delete, delete-orphan"
                          )
