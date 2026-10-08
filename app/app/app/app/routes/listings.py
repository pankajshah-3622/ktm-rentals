from fastapi import APIRouter

router = APIRouter(prefix="/listings", tags=["Listings"])

@router.get("/")
def get_listings():
    return [{"id": 1, "title": "1 BHK Room in Jhamsikhel", "price": 15000}]