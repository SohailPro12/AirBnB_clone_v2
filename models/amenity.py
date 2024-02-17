#!/usr/bin/python3
"""The class of the Amenity"""
from models.base_model import BaseModel, Base
import models
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    """The class for Amenity with name as an attribute"""
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(
            String(128),
            nullable=False
        )
        place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            back_populates="amenities"
        )
    else:
        name = ""
