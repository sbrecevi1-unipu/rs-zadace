from fastapi import FastAPI, HTTPException
from models import Vrijeme

from aiohttp import ClientSession

import xml.etree.ElementTree as ET
from fastapi import status


app = FastAPI()

@app.get("/regije/{kljuc}")
async def get_regije(kljuc : str):

    async with ClientSession() as session:
        response = await session.get(f"http://regije_mikroservice:4000/regije/{kljuc}")
        response_json = await response.json()
    return response_json

@app.get("/vrijeme", response_model=list[Vrijeme])
async def dohvati_vrijeme():
    url = "https://prognoza.hr/prognoza_sutra.xml"
    try:
        async with ClientSession() as session:
            response = await session.get(url)
            if response.status != 200: # u slučaju greške
                raise HTTPException(status_code=response.status, detail="Greška u dohvaćanju XML podataka s DHMZ API-ja")
            xml_data = await response.text()
    except Exception as e: # Uhvati sve greške ako dođe do problema u slanju zahtjeva
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Greška u slanju HTML zahtjeva na DHMZ API")

    root = ET.fromstring(xml_data)
    stations = root.findall(".//station")
    weather_list = []
    
    for station in stations: # iteriraj kroz sve station elemente i izvuci podatke
        mjesto = station.attrib.get("name")
        temperatura_min = int(station.find("./param[@name='Tmn']").attrib.get("value"))
        temperatura_max = int(station.find("./param[@name='Tmx']").attrib.get("value"))
        vjetar = int(station.find("./param[@name='wind']").attrib.get("value"))
        weather_list.append(Vrijeme(
                    mjesto=mjesto,
                    temperatura_min=temperatura_min,
                    temperatura_max=temperatura_max,
                    vjetar=vjetar
                ))
    return weather_list