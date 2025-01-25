
from pydantic import BaseModel

#                   {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
#                   {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
#                   {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
#                   {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}


class Film(BaseModel):
    id     : int
    naziv  : str
    genre  : str
    godina : int

class CreateFilm(BaseModel):
    naziv  : str
    genre  : str
    godina : int