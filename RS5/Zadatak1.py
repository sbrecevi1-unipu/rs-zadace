'''
Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji/proizvodi 
vraća listu proizvoda u JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve 
naziv , cijena i količina . Pošaljite zahtjev na adresu http://localhost:8081/proizvodi 
koristeći neki od HTTP klijenata ili curl i provjerite odgovor.

Now Playing
Fast As A Shark  by  Accept
'''

import asyncio
# import aiohttp

from aiohttp import web


def handler_function(request):
    # Kreiranje liste proizvoda - proizvod je riječnik listi
    products = [
        {
            "naziv": "Proizvod 1",
            "cijena": 10.0,
            "kolicina": 5
        },
        {
            "naziv": "Proizvod 2",
            "cijena": 20.0,
            "kolicina": 3
        },
        {
            "naziv": "Proizvod 3",
            "cijena": 15.5,
            "kolicina": 10
        }
    ]
    
    return web.json_response(products)
    

   

app = web.Application()

app.router.add_get("/prozvodi", handler_function)
# web.run_app(app, port=8081)
web.run_app(app, host='localhost', port=8081)
