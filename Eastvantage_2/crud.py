                                     
from sqlalchemy.orm import Session   
import models, schemas, utils        


# Create a new address in the database
def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(**address.dict())     # Convert Pydantic model to dictionary, unpack into SQLAlchemy model

    # Add and commit to database
    db.add(db_address)
    db.commit()
    db.refresh(db_address)    # Refresh to get updated state from DB (e.g., auto-generated id)

    return db_address


# Retrieve all addresses from the database
def get_addresses(db: Session):
    return db.query(models.Address).all()


# Update an existing address by ID (full replacement of fields)
def update_address(db: Session, address_id: int, address: schemas.AddressCreate):
   
    # Find the address
    db_address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not db_address:
        raise Exception("Address not found")

    # Replace each field with new values from request
    for key, value in address.dict().items():
        setattr(db_address, key, value)

    # Commit changes
    db.commit()
    db.refresh(db_address)

    return db_address

# Delete an address by ID
def delete_address(db: Session, address_id: int):
    db_address = db.query(models.Address).filter(models.Address.id == address_id).first()
    if not db_address:
        raise Exception("Address not found")

    db.delete(db_address)
    db.commit()


# Get addresses within a given distance from a reference point
def get_addresses_within_distance(db: Session, lat: float, lon: float, distance_km: float):
   
    # Fetch all addresses (in a real large-scale app, use spatial queries instead)
    all_addresses = db.query(models.Address).all()

    # Filter only addresses within distance_km
    return [
        addr for addr in all_addresses
        if utils.haversine(lat, lon, addr.latitude, addr.longitude) <= distance_km
    ]
