# pyright: reportMissingImports=false
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app import models

# Auto-create tables in PostgreSQL database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="KTM Rentals API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for POST requests
class ListingCreate(BaseModel):
    title: str
    location: str
    price: float
    floor_level: str
    water_facility: str
    parking_available: bool = True
    is_verified_owner: bool = True

@app.get("/")
def read_root():
    return {"status": "API is online"}

@app.get("/listings")
def get_listings(db: Session = Depends(get_db)):
    listings = db.query(models.Listing).all()
    
    # Seed initial dummy data if DB is empty
    if not listings:
        dummy_listing = models.Listing(
            title="Spacious 2 BHK Flat Near Pulchowk Campus",
            location="Lalitpur",
            price=25000.0,
            floor_level="2nd Floor",
            water_facility="Melamchi + Underground Tanker",
            parking_available=True,
            is_verified_owner=True
        )
        db.add(dummy_listing)
        db.commit()
        db.refresh(dummy_listing)
        listings = [dummy_listing]
        
    return listings

@app.post("/listings")
def create_listing(listing: ListingCreate, db: Session = Depends(get_db)):
    new_listing = models.Listing(**listing.dict())
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing