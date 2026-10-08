from fastapi import FastAPI

app = FastAPI(title="KTM Rentals API")

@app.get("/")
def read_root():
    return {"message": "Welcome to KTM Rentals Backend Service"}