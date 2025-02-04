from pydantic import BaseModel, validator, Field, HttpUrl
from typing import List, Optional
import re


class Actor(BaseModel):
    name: str
    surname: str


class Writer(BaseModel):
    name: str
    surname: str


def split_name_surname(full_name: str) -> (str, str):
    """
    Pomoćna funkcija koja prima cijelo ime
    (npr. 'Sam Worthington' ili 'Akiva Goldsman (screenplay)'),
    te pokušava razdvojiti u name i surname.
    Ovdje radimo jednostavno:
      - uklonimo sve što je u zagradama
      - podijelimo na riječi
      - prvu riječ uzimamo kao 'name', a sve ostalo spojimo kao 'surname'.
    """
    # Ukloni sadržaj u zagradama (ako postoji)
    full_name = re.sub(r"\(.*?\)", "", full_name).strip()

    parts = full_name.split()
    if len(parts) == 1:
        return parts[0], ""  # samo ime, bez prezimena
    return parts[0], " ".join(parts[1:])


class Movie(BaseModel):
    # Obavezni atributi:
    Title: str
    Year: int                # želimo int, ne string
    Rated: str
    Runtime: int             # želimo int (broj minuta), ne string "162 min"
    Genre: str
    Language: str
    Country: str
    Actors: List[Actor]      # dobit ćemo listu iz custom validacije
    Plot: str
    Writer: List[Writer]

    # Ostali, neobavezni (default=None ili sl.):
    Director: Optional[str] = None
    Awards: Optional[str] = None
    Poster: Optional[str] = None
    Metascore: Optional[str] = None
    imdbRating: Optional[float] = None    # 0.0 - 10.0
    imdbVotes: Optional[int] = None       # >0
    imdbID: Optional[str] = None
    Type: Optional[str] = None            # "movie" ili "series"
    Response: Optional[str] = None
    totalSeasons: Optional[str] = None
    ComingSoon: Optional[bool] = None
    Images: Optional[List[HttpUrl]] = None

    # VALIDATORI

    @validator("Actors", pre=True)
    def parse_actors(cls, v):
        """
        Pretpostavljamo da nam 'v' dolazi kao string tipa:
        'Sam Worthington, Zoe Saldana, Sigourney Weaver, ...'
        Odvojimo ih po zarezu i pretvorimo svaki u Actor.
        """
        if isinstance(v, str):
            actor_strings = [s.strip() for s in v.split(",")]
            actors = []
            for a_str in actor_strings:
                name, surname = split_name_surname(a_str)
                actors.append(Actor(name=name, surname=surname))
            return actors
        return v  # ako nije string, pretpostavimo da je već lista

    @validator("Writer", pre=True)
    def parse_writers(cls, v):
        """
        Slično parse_actors:
        'Mark Protosevich (screenplay), Akiva Goldsman (screenplay), Richard Matheson (novel)'
        -> lista Writer objekata
        """
        if isinstance(v, str):
            writer_strings = [s.strip() for s in v.split(",")]
            writers = []
            for w_str in writer_strings:
                name, surname = split_name_surname(w_str)
                writers.append(Writer(name=name, surname=surname))
            return writers
        return v

    @validator("Type")
    def validate_type(cls, v):
        """
        Provjera da je tip 'movie' ili 'series', ako je uopće zadano.
        """
        if v is None:
            return None
        allowed = {"movie", "series"}
        if v not in allowed:
            raise ValueError(f"Type mora biti 'movie' ili 'series', dobiveno: {v}")
        return v

    @validator("Year", pre=True)
    def parse_year(cls, v):
        """
        Neki filmovi imaju '2011–' (kod serija). Izvucimo samo prvi dio.
        """
        # Dohvati prve 4 znamenke
        match = re.match(r"(\d{4})", str(v))
        if not match:
            raise ValueError(f"Neispravan format Year: {v}")
        return int(match.group(1))

    @validator("Year")
    def validate_year(cls, v):
        if v < 1900:
            raise ValueError("Godina mora biti veća od 1900")
        return v

    @validator("Runtime", pre=True)
    def parse_runtime(cls, v):
        """
        '162 min' -> 162 (int)
        """
        # Izvuci samo broj
        match = re.match(r"(\d+)", str(v))
        if not match:
            raise ValueError(f"Neispravan format Runtime: {v}")
        return int(match.group(1))

    @validator("Runtime")
    def validate_runtime(cls, v):
        if v <= 0:
            raise ValueError("Runtime mora biti veći od 0.")
        return v

    @validator("imdbRating", pre=True, always=True)
    def parse_rating(cls, v):
        """
        Ako je 'N/A' ili None, tretiramo kao None.
        Inače parsiramo float i validiramo 0-10.
        """
        if v is None or v == "N/A":
            return None
        try:
            return float(v)
        except ValueError:
            return None

    @validator("imdbRating")
    def validate_rating(cls, v):
        if v is not None and (v < 0 or v > 10):
            raise ValueError("imdbRating mora biti između 0 i 10.")
        return v

    @validator("imdbVotes", pre=True, always=True)
    def parse_votes(cls, v):
        """
        '890,617' -> 890617
        Ako je 'N/A' ili None -> None
        """
        if v is None or v == "N/A":
            return None
        # Ukloni zareze
        v_str = str(v).replace(",", "")
        try:
            return int(v_str)
        except ValueError:
            return None

    @validator("imdbVotes")
    def validate_votes(cls, v):
        if v is not None and v <= 0:
            raise ValueError("imdbVotes mora biti veći od 0.")
        return v
