'''
Definirajte poslužitelj koji sluša na portu 8082 i na putanji /punoljetni 
vraća listu korisnika starijih od 18 godina. Svaki korisnik je rječnik koji sadrži
ključeve ime i godine . Pošaljite zahtjev na adresu 
http://localhost:8082/punoljetni i provjerite odgovor. 
Novu listu korisnika definirajte koristeći funkciju filter ili list comprehension .
'''
from aiohttp import web
import asyncio

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def handler_function(request):
    punoljetni = [i for i in korisnici if i['godine']>=18]

    return web.json_response(punoljetni, status = 200)


def main(): # main korutina (asinkrona funkcija)
    app = web.Application()

    app.router.add_get("/punoljetni", handler_function)
    web.run_app(app, port=8082)
    

main()