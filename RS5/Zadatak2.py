'''
Nadogradite poslužitelj iz prethodnog zadatka na način da na istoj putanji 
/proizvodi prima POST zahtjeve s podacima o proizvodu. Podaci se šalju u JSON
formatu i sadrže ključeve naziv , cijena i količina . Handler funkcija treba 
ispisati primljene podatke u terminalu, dodati novi proizvod u listu proizvoda i
vratiti odgovor s novom listom proizvoda u JSON formatu.

Now Playing
I Don't Believe In Love  by  Queensrÿche

'''

import asyncio
# import aiohttp
import json

from aiohttp import web

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

def handler_function(request):
       
    try:
        return web.json_response(proizvodi)
    except Exception as e:
        return web.Response(status=400, text="Bad Request")

async def handler_function2(request):
    # print(type(request))
    # print(await request.json())
    for i in await request.json():
        proizvodi.append(i)
    print(proizvodi)
    
    return web.json_response(proizvodi)
    # return web.json_response(text='primio sam podatke')

    pass
    

   

app = web.Application()
app.router.add_get("/proizvodi", handler_function)
# i nakon get-a opet vraća dopunjene proizvode dok je god program u memoriji
# TOP koncept... Nikad radio "server" koji geta i posta... 
# sad mi je jasnije kako to radi kada ja dohvaćam podatke sa e-Ovrha...
# još mi je manje jasno zašto kako im upiti međusobno nisu usklađeni... 
# Pa su disableali endpoint za svih jer im je upit timeout-ao...
app.router.add_post("/proizvodi", handler_function2)
# web.run_app(app, port=8081)
web.run_app(app, host='localhost', port=8081)
