from pydantic import BaseModel,Field
from datetime import datetime
from typing import List, Literal, Dict, Tuple
from typing_extensions import TypedDict


# Definirajte Pydantic model RestaurantOrder koji se sastoji od 
# informacija o narudžbi u restoranu.
# Narudžba se sastoji od identifikatora, imena kupca, stol_info, liste 
# jela i ukupne cijene. Definirajte još jedan model za jelo koje se 
# sastoji od identifikatora, naziva i cijene. 
# Za stol_info pohranite rječnik koji očekuje ključeve broj i lokacija . 
# Primjerice, stol_info može biti {"broj": 5, "lokacija": "terasa"}. 
# Za definiciju takvog rječnika koristite TypedDict tip iz modula typing .

class Knjiga(BaseModel):
    naslov          : str
    ime_autora      : str
    prezime_autora  : str
    godina_izdanja  : int = Field(default_factory = lambda: datetime.now().year)
    broj_stranica   : int
    izdavac         : str


class Izdavač(BaseModel):
    naziv           : str
    adresa          : str

class Admin(BaseModel):
    ime             : str
    prezime         : str
    username        : str
    email           : str
    ovlasti         : List[Literal['dodavanje' , 'brisanje' , 'ažuriranje' , 'čitanje']]



    

class Jelo(BaseModel):
    identifikator   : int
    naziv           : str
    cijena          : float

class StolInfo(TypedDict):
    broj            : int
    lokacija        : str

class RestaurantOrder(BaseModel):
    identifikator   : int
    ime_kupca       : str
    stol_info       : StolInfo 
    lista_jela      : List[Jelo]
    ukupna_cijena   : float


class CCTV_frame(BaseModel):
    identifikator   : int
    vrijeme_snimanja: datetime
    koordinate      : Tuple[float,float]=Field(default=(0.0,0.0))


narudzba = RestaurantOrder(
    identifikator=1,
    ime_kupca="Ivana Horvat",
    stol_info={"broj": 5, "lokacija": "terasa"},
    lista_jela=[
        Jelo(identifikator=1, naziv="Pizza", cijena=50.0),
        Jelo(identifikator=2, naziv="Salata", cijena=30.0)
    ],
    ukupna_cijena=80.0
)
frame = CCTV_frame(identifikator=1,
    vrijeme_snimanja=datetime.now(),
    koordinate=(45.8150, 15.9819))

print(narudzba)
print(frame)