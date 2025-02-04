from fastapi import FastAPI
from routers import filmovi

app = FastAPI(
    title="Movies API",
    description="Mikroservis za dohvaćanje podataka o filmovima (Filtriranje, dohvat, validacije)",
    version="1.0.0"
)

# Uključujemo rute iz filmovi.py
app.include_router(filmovi.router, prefix="/filmovi", tags=["filmovi"])


@app.get("/")
def root():
    return {"message": "Dobrodošli u Movies API!"}
