# Address model

from sqlalchemy import Column, Integer, String, Float
from database import Base  # This is our declarative base from database.py

# Define a database table called "addresses"
class Address(Base):
    __tablename__ = "addresses"  # Table name in the database

    # Primary key column - unique for each record, auto-incremented
    id = Column(Integer, primary_key=True, index=True)

    # Name of the address/location
    # String type, cannot be NULL in the database
    name = Column(String, nullable=False)

    # Latitude coordinate of the location
    # Float type, cannot be NULL
    latitude = Column(Float, nullable=False)

    # Longitude coordinate of the location
    # Float type, cannot be NULL
    longitude = Column(Float, nullable=False)
