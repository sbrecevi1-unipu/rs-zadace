from fastapi import FastAPI,HTTPException
from models import Film,CreateFilm


app = FastAPI()

filmovi = [
        {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
        {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
        {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
        {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
        ]

@app.get("/filmovi")
def get_filmovi(genre: str = None, min_godina: int=2000):
    filtrirani_filmovi=[
        film for film in filmovi
        if (genre is None or film["genre"] == genre) and film["godina"]>=min_godina

    ]
    
    return filtrirani_filmovi

@app.get("/filmovi/{id}", response_model=Film)
def read_item(id: int):
    for film in filmovi:
        if film["id"]==id:
            return film
        
    
    raise HTTPException(status_code=404, detail="Film nije pronađen")
    
@app.post("/filmovi", response_model=CreateFilm)
def create_film(novi_film:CreateFilm):
    id = max(film["id"]for film in filmovi) + 1 if filmovi else 1
    film_dict["id"] = id
    film_dict = novi_film.dict()

    # Dodavanje novog filma u listu
    filmovi.append(film_dict)
    return film_dict