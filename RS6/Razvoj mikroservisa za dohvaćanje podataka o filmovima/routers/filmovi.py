from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import json
import os

from models.models import Movie

router = APIRouter()

# Globalna in-memory lista filmova
movies_db: List[Movie] = []


@router.on_event("startup")
def load_movies_from_json():
    """
    Ova će se funkcija pozvati pri pokretanju aplikacije.
    Učitava 'data/movies.json', deserializira svaki film u Movie,
    i pohranjuje u movies_db.
    """
    
    json_path = "filmovi.json"

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)  # list of dict
        for item in data:
            # Pokušaj parsirati u Movie
            try:
                m = Movie(**item)
                movies_db.append(m)
            except Exception as e:
                # Ako dođe do greške u validaciji, možete je ispisati ili ignorirati
                print(f"[WARN] Neuspješno parsiranje filma: {item.get('Title')} -> {e}")


@router.get("/", response_model=List[Movie])
def get_all_movies(
    min_year: Optional[int] = Query(None, ge=1900),
    max_year: Optional[int] = Query(None, ge=1900),
    min_rating: Optional[float] = Query(None, ge=0, le=10),
    max_rating: Optional[float] = Query(None, ge=0, le=10),
    type: Optional[str] = Query(None, regex="^(movie|series)$"),
) -> List[Movie]:
    """
    Vraća sve filmove uz mogućnost filtriranja:
      - min_year, max_year (>= 1900)
      - min_rating, max_rating (0-10)
      - type (movie ili series)
    """
    filtered = []
    for film in movies_db:
        # Filtriranje po godini
        if min_year is not None and film.Year < min_year:
            continue
        if max_year is not None and film.Year > max_year:
            continue

        # Filtriranje po ocjeni
        # imdbRating može biti None, pa pazimo
        if min_rating is not None:
            if film.imdbRating is None or film.imdbRating < min_rating:
                continue
        if max_rating is not None:
            if film.imdbRating is None or film.imdbRating > max_rating:
                continue

        # Filtriranje po type
        if type is not None:
            if film.Type != type:
                continue

        filtered.append(film)

    return filtered


@router.get("/{imdb_id}", response_model=Movie)
def get_movie_by_imdb_id(imdb_id: str) -> Movie:
    """
    Dohvati film prema imdbID (npr. 'tt0499549').
    Ako ne postoji, bacamo 404.
    """
    for film in movies_db:
        if film.imdbID == imdb_id:
            return film
    raise HTTPException(status_code=404, detail="Film s danim imdbID ne postoji.")


@router.get("/title/{title}", response_model=Movie)
def get_movie_by_title(title: str) -> Movie:
    """
    Dohvati film prema Title.
    Ako ne postoji, bacamo 404.
    """
    # Case-insensitive pretraga (ako želite)
    title_lower = title.lower()
    for film in movies_db:
        if film.Title.lower() == title_lower:
            return film

    raise HTTPException(status_code=404, detail="Film s danim Title ne postoji.")
