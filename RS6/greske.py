from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI()

# Zajednički Pydantic model za osnovne atribute automobila
class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int = Field(gt=1960, description="Godina proizvodnje mora biti veća od 1960")
    boja: str

# Model za unos automobila (korisnik ne šalje ID ni cijenu s PDV-om)
class CarInput(BaseCar):
    cijena: float = Field(gt=0, description="Cijena mora biti veća od 0")

# Model za pohranu automobila (uključuje ID i cijenu s PDV-om)
class CarOutput(BaseCar):
    id: int
    cijena: float
    cijena_pdv: float

# Simulirana baza podataka
automobili_db: List[CarOutput] = [
    CarOutput(id=1, marka="Dacia", model="Spring", godina_proizvodnje=2022, cijena=15000.0, cijena_pdv=18750.0, boja="plava"),
    CarOutput(id=2, marka="Renault", model="Espace", godina_proizvodnje=2007, cijena=3000.0, cijena_pdv=3750.0, boja="siva"),
    CarOutput(id=3, marka="Citroen", model="C4", godina_proizvodnje=2006, cijena=2000.0, cijena_pdv=2500.0, boja="bijela"),
]

# Ruta za dohvaćanje svih automobila
@app.get("/automobili", response_model=List[CarOutput])
def get_svi_automobili():
    return automobili_db

# Ruta za dohvaćanje automobila prema ID-u
@app.get("/automobili/{automobil_id}", response_model=CarOutput)
def get_automobil(automobil_id: int):
    # Pronađi automobil u "bazi podataka"
    for automobil in automobili_db:
        if automobil.id == automobil_id:
            return automobil
    # Ako automobil nije pronađen, podigni HTTPException
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")

# Ruta za dodavanje novog automobila
@app.post("/automobili", response_model=CarOutput)
def dodaj_automobil(automobil: CarInput):
    # Provjera postoji li automobil već u bazi
    for a in automobili_db:
        if a.marka == automobil.marka and a.model == automobil.model and a.godina_proizvodnje == automobil.godina_proizvodnje:
            raise HTTPException(status_code=400, detail="Automobil već postoji u bazi podataka.")

    # Generiranje ID-a i cijene s PDV-om
    novi_id = max([a.id for a in automobili_db], default=0) + 1
    cijena_pdv = round(automobil.cijena * 1.25, 2)  # Pretpostavljena PDV stopa od 25%

    # Kreiranje novog automobila i dodavanje u bazu
    novi_automobil = CarOutput(
        id=novi_id,
        marka=automobil.marka,
        model=automobil.model,
        godina_proizvodnje=automobil.godina_proizvodnje,
        cijena=automobil.cijena,
        cijena_pdv=cijena_pdv,
        boja=automobil.boja,
    )
    automobili_db.append(novi_automobil)
    return novi_automobil
