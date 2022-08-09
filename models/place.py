#!/usr/bin/python3
""" Place Module for HBNB project """
from models import review
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    name = Column(String(128), nullable=False)

    description = Column(String(1024), nullable=True)

    number_rooms = Column(Integer, nullable=False, default=0)

    number_bathrooms = Column(Integer, nullable=False, default=0)

    max_guest = Column(Integer, nullable=False, default=0)

    price_by_night = Column(Integer, nullable=False, default=0)

    latitude = Column(Float, nullable=True)

    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref="place")

    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Lists all reviews"""
            all_reviews = self.reviews
            reviews_array = []
            for key, value in all_reviews.items():
                if self.id == value.review_id:
                    reviews_array.append(value)

            return reviews_array

        @property
        def amenities(self):
            """Lists all amenities"""
            all_amenities = self.amenities
            amenities_array = []
            for key, value in all_amenities.items():
                if self.id == value.amenities_id:
                    amenities_array.append(value)

            return amenities_array

        @amenities.setter
        def amenities(self, value=None):
            amenity_ids = []
            """Sets the list"""
            if value is not None:
                for amenity in models.storage.all("Amenity").value():
                    if amenity.place_id == self.id:
                        amenity_ids.append(value)


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60), 
                             ForeignKey("amenities.id"), primary_key=True,
                             nullable=False)
                      )
