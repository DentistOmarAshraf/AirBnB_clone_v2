#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete",
                              back_populates="state")

    else:
        name = ""

        @property
        def cities(self):
            the_cities = []
            for x, v in models.storage.all(City).items():
                if v.state_id == self.id:
                    the_cities.append(v)

            return the_cities
