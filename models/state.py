#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",  backref="state", cascade="all, delete")
    else:
        @property
        def city_instances(self):
            """list of City instances with state_id
            equals to the current State.id for FileStorage"""
            city_instances = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_instances.append(city)
            return city_instances
