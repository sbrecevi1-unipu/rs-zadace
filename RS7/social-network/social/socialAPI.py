from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, constr
from typing import List
import datetime
import aiohttp
import json

app = FastAPI()

class ObjavaCreate(BaseModel):
    korisnik: constr(max_length=20)
    tekst: constr(max_length=280)
    vrijeme: datetime.datetime

class Objava(ObjavaCreate):
    id: int

class UserCredentials(BaseModel):
    korisnicko_ime: str
    lozinka: str

objave = []
counter = 1

async def verify_credentials(credentials: UserCredentials) -> bool:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(
                'http://auth:9000/login',
                json={
                    'korisnicko_ime': credentials.korisnicko_ime,
                    'lozinka': credentials.lozinka
                }
            ) as response:
                if response.status == 200:
                    return True
                return False
        except aiohttp.ClientError as e:
            raise HTTPException(
                status_code=500, 
                detail=f"Error communicating with auth service: {str(e)}"
            )

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

@app.post("/korisnici/{korisnik}/objave", response_model=List[Objava])
async def get_korisnik_objave(korisnik: str, credentials: UserCredentials):
    # Verify credentials
    is_authorized = await verify_credentials(credentials)
    if not is_authorized:
        raise HTTPException(
            status_code=401, 
            detail="Neispravni korisnički podaci"
        )
    
    # If authorized, return posts
    korisnik_objave = [o for o in objave if o.korisnik == korisnik]
    return korisnik_objave