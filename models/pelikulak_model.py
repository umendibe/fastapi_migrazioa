from pydantic import BaseModel


class Pelikulak(BaseModel):
    izenburua: str
    generoa: str
    iraupena: int
    

class PelikulakPatch(BaseModel):
    izenburua: str | None = None
    generoa: str | None = None
    iraupena: int | None = None