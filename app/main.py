from fastapi import FastAPI, Depends
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

@app.get("/")
def read_root():
    return {"status": "API is online"}

@app.get("/listings")
def get_listings(db: Session = Depends(get_db)):
    # Fetch all listings from PostgreSQL database
    listings = db.query(models.Listing).all()
    
    # Seed dummy data if database table is empty
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