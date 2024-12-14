'''
Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji/proizvodi 
vraća listu proizvoda u JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve 
naziv , cijena i količina . Pošaljite zahtjev na adresu http://localhost:8081/proizvodi 
koristeći neki od HTTP klijenata ili curl i provjerite odgovor.

Now Playing
Fast As A Shark  by  Accept

It lasted a few songs more to find misspelled pro(i)zvodi, 
dok sam doma flame-ao firmu na restriktivnom firewallu 
i ludom antivirusnom softwareu koji mi exeove Pythona inače trpa u karantenu

'''

import asyncio
# import aiohttp
import json

from aiohttp import web


def handler_function(request):
    # Kreiranje liste proizvoda - proizvod je riječnik listi
    proizvodi = [
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
    try:
        # Process the request
        
        # return web.Response(text=json.dumps(proizvodi))
    #ili
        return web.json_response(proizvodi)
    except Exception as e:
        return web.Response(status=400, text="Bad Request")

    

   

app = web.Application()

app.router.add_get("/proizvodi", handler_function)
# web.run_app(app, port=8081)
web.run_app(app, host='localhost', port=8081)
