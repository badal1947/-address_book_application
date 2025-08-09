# FastAPI app

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
import models, crud, schemas, utils

# Create all tables defined in models.Base in the database (if they don't exist already)
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application with a title
app = FastAPI(title="Address Book API")


# Dependency function to get a database session
# This is used in endpoints via `Depends(get_db)`
def get_db():
    db = SessionLocal()  # Create a new DB session
    try:
        yield db  # Provide the session to the path operation function
    finally:
        db.close()  # Always close the session after use


# POST /addresses/
# Create a new address in the database
@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)


# GET /addresses/
# Return all addresses in the database
@app.get("/addresses/", response_model=List[schemas.Address])
def list_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)


# PUT /addresses/{address_id}
# Update an existing address entirely
@app.put("/addresses/{address_id}", response_model=schemas.Address)
def update_address(address_id: int, address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.update_address(db, address_id, address)


# DELETE /addresses/{address_id}
# Remove an address from the database
@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    crud.delete_address(db, address_id)
    return {"detail": "Address deleted"}


# GET /addresses/nearby/
# Returns all addresses within a given distance from a given point
@app.get("/addresses/nearby/", response_model=List[schemas.Address])
def get_nearby_addresses(lat: float, lon: float, distance_km: float, db: Session = Depends(get_db)):
    return crud.get_addresses_within_distance(db, lat, lon, distance_km)
