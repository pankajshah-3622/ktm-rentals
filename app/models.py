from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    location = Column(String, index=True) # e.g., Jhamsikhel, Baneshwor
    price = Column(Float)
    floor_level = Column(String) # Ground, 1st, 2nd, Top
    water_facility = Column(String) # Melamchi, Boring, Tanker
    parking_available = Column(Boolean, default=True)
    is_verified_owner = Column(Boolean, default=True) # Broker protection flag