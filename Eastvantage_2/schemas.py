# Pydantic validation

# Import Pydantic's BaseModel for defining data models
# Field is used for extra validation & metadata
# validator is used to run custom validation functions
from pydantic import BaseModel, Field, validator

# Base schema for shared fields between input & output
class AddressBase(BaseModel):
    # Name must be at least 1 character long
    name: str = Field(..., min_length=1)

    # Latitude as a float (-90 to +90 degrees)
    latitude: float

    # Longitude as a float (-180 to +180 degrees)
    longitude: float

    # Custom validator for latitude
    @validator("latitude")
    def validate_latitude(cls, v):
        if not -90 <= v <= 90:
            raise ValueError("Latitude must be between -90 and 90")
        return v

    # Custom validator for longitude
    @validator("longitude")
    def validate_longitude(cls, v):
        if not -180 <= v <= 180:
            raise ValueError("Longitude must be between -180 and 180")
        return v


# Schema for creating an address (same as base, no extra fields)
class AddressCreate(AddressBase):
    pass


# Schema for returning an address from the API (includes DB id)
class Address(AddressBase):
    id: int  # Read-only ID field from the database

    class Config:
        from_attributes = True
        # orm_mode tells Pydantic it can read SQLAlchemy model objects
        # directly and convert them to this schema
