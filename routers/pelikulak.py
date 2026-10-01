from fastapi import APIRouter, HTTPException

from pydantic import BaseModel

pelikulak_router = APIRouter(
    prefix="/pelikulak",
    tags=["PELIKULAK"]
)

pelikulak_db = [
    {"id": 1, "izenburua": "Dune", "generoa": "Zientzia-fikzioa", "iraupena": 155},
    {"id": 2, "izenburua": "Coco", "generoa": "Animazioa", "iraupena": 105},
    {"id": 3, "izenburua": "Alien", "generoa": "Zientzia-fikzioa", "iraupena": 117},
    {"id": 4, "izenburua": "Gladiator", "generoa": "Akzioa", "iraupena": 155},
]

@pelikulak_router.get("")
def get_pelikula_guztiak():
    if pelikulak_db:
        return pelikulak_db
    raise HTTPException(status_code=404, detail="Ez dira pelikulak aurkitu")



@pelikulak_router.get("/generoa/{generoa}")
def get_pelikulak_generoa(generoa: str):
    pelikulak_filtratuak = []
    for pelikula in pelikulak_db:
        if pelikula["generoa"].upper() == generoa.upper():
            pelikulak_filtratuak.append(pelikula)
    if not pelikulak_filtratuak:
        raise HTTPException(status_code=404, detail="Ez da aurkitu genero hontako pelikulak")
    return pelikulak_filtratuak
    


@pelikulak_router.get("/id/{id}")
def get_pelikulak_id(id: int):
    for pelikula in pelikulak_db:
        if pelikula["id"] == id:
            return pelikula
    raise HTTPException(status_code=404, detail="Ez da aurkitu pelikula")



class Pelikulak(BaseModel):
    izenburua: str
    generoa: str
    iraupena: int
    
@pelikulak_router.post("", status_code=201)
def post_pelikula(pelikula_berria: Pelikulak):
    id_berria = pelikulak_db[-1]["id"] + 1 if pelikulak_db else 1
    pelikulak_dict = pelikula_berria.model_dump()
    pelikulak_dict["id"] = id_berria
    pelikulak_db.append(pelikulak_dict)
    return pelikulak_dict

@pelikulak_router.put("/update/{id}")
def put_pelikula(id: int):
    pass







    


        
