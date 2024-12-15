'''
Prvi mikroservis neka sluša na portu 8083 i na endpointu /zbroj vraća JSON bez čekanja. Ulazni podatak u tijelu zahtjeva neka bude lista
brojeva, a odgovor neka bude zbroj svih brojeva. Dodajte provjeru ako brojevi nisu proslijeđeni, vratite
odgovarajući HTTP odgovor i statusni kod.
Drugi mikroservis neka sluša na portu 8084 te kao ulazni podataka prima iste podatke. Na endpointu
/umnozak neka vraća JSON odgovor s umnoškom svih brojeva. Dodajte provjeru ako brojevi nisu
proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kod.
 Dodajte provjeru i vratite odgovarajući statusni kod ako se pokuša umnožak dijeliti s 0.
U client.py pozovite konkurentno s proizvoljnim podacima prva dva mikroservisa, a zatim sekvencijalno
pozovite treći mikroservis.
'''

import asyncio
import aiohttp
from aiohttp import web
import json


async def zbroj(request):

    try:
        zbroj = 0
        data = await request.json()
        
        for _ in data['podaci']:
            zbroj += _ 
        zbroj_dict = {
            'zbroj': zbroj
        }
        return web.json_response(zbroj_dict, status = 200)
    except:
        return web.json_response('Method Not Allowed', status = 405)
        pass
    




app = web.Application()
app.router.add_post('/zbroj', zbroj)


if __name__ == "__main__":
    web.run_app(app, port=8083)
