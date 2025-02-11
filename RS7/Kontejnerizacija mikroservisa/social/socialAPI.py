from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import List
import datetime

app = FastAPI()

class ObjavaCreate(BaseModel):
    korisnik: constr(max_length=20)
    tekst: constr(max_length=280)
    vrijeme: datetime.datetime

class Objava(ObjavaCreate):
    id: int

objave = []
counter = 1

@app.post("/objava", response_model=Objava)
async def create_objava(objava: ObjavaCreate):
    global counter
    nova_objava = Objava(
        id=counter,
        korisnik=objava.korisnik,
        tekst=objava.tekst,
        vrijeme=objava.vrijeme
    )
    objave.append(nova_objava)
    counter += 1
    return nova_objava

@app.get("/objava/{id}", response_model=Objava)
async def get_objava(id: int):
    objava = next((o for o in objave if o.id == id), None)
    if not objava:
        raise HTTPException(status_code=404, detail="Objava nije pronađena")
    return objava

@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
async def get_korisnik_objave(korisnik: str):
    korisnik_objave = [o for o in objave if o.korisnik == korisnik]
    return korisnik_objave