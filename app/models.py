from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    location = Column(String, index=True)
    price = Column(Float)
    floor_level = Column(String)
    water_facility = Column(String)
    parking_available = Column(Boolean, default=True)
    is_verified_owner = Column(Boolean, default=True)