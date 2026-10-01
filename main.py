from fastapi import FastAPI

from routers import pelikulak

app = FastAPI()

app.include_router(pelikulak.pelikulak_router)

app.get("/")
def ongietorria():
    return {"Pelikulen orria"}