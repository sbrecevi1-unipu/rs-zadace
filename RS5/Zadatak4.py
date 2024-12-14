'''
Definirajte aiohttp poslužitelj koji radi na portu 8081 . Poslužitelj mora imati dvije rute: /proizvodi i
/proizvodi/{id} . Prva ruta vraća listu proizvoda u JSON formatu, a druga rutu vraća točno jedan proizvod
prema ID-u. Ako proizvod s traženim ID-em ne postoji, vratite odgovor s statusom 404 i porukom
{'error': 'Proizvod s traženim ID-em ne postoji'} .
Proizvode pohranite u listu rječnika:
proizvodi = [
{"id": 1, "naziv": "Laptop", "cijena": 5000},
{"id": 2, "naziv": "Miš", "cijena": 100},
{"id": 3, "naziv": "Tipkovnica", "cijena": 200},
{"id": 4, "naziv": "Monitor", "cijena": 1000},
{"id": 5, "naziv": "Slušalice", "cijena": 50}
]
Testirajte poslužitelj na sve slučajeve kroz klijentsku sesiju unutar main korutine iste skripte.
'''

from aiohttp import web
import asyncio, aiohttp

import asyncio



proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]




async def get_function(request):
    return web.json_response(proizvodi)

async def get_function_by_id(request):

    try:
        # Dohvat ID-a iz URL-a
        proizvod_id = int(request.match_info['id'])
    except ValueError:
        return web.json_response(
            {"error": "ID mora biti cijeli broj"}, status=400
        )

    # Pronalaženje proizvoda s odgovarajućim ID-em
    proizvod = next((p for p in proizvodi if p['id'] == proizvod_id), None)

    if proizvod:
        return web.json_response(proizvod)
    else:
        return web.json_response(
            {"error": "Proizvod s traženim ID-em ne postoji"}, status=404
        )
    
# Klijentska sesija za testiranje
async def test_client():
    await asyncio.sleep(1)  # Allow server to start
    async with aiohttp.ClientSession() as session:
        # Testiranje svih proizvoda
        async with session.get('http://localhost:8081/proizvodi') as resp:
            print("GET /proizvodi:", await resp.json())

        # Testiranje proizvoda po ID-u
        async with session.get('http://localhost:8081/proizvodi/1') as resp:
            print("GET /proizvodi/1:", await resp.json())

        # Testiranje proizvoda koji ne postoji
        async with session.get('http://localhost:8081/proizvodi/999') as resp:
            print("GET /proizvodi/999:", await resp.json())

        # Testiranje neispravnog ID-a
        async with session.get('http://localhost:8081/proizvodi/abc') as resp:
            print("GET /proizvodi/abc:", await resp.json())
    
async def post_function(request):
    return web.json_response({'message': 'POST request received'})


app = web.Application()
app.router.add_get('/proizvodi', get_function)
app.router.add_get('/proizvodi/{id}', get_function_by_id)
app.router.add_post('/', post_function)


async def start_server():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host='localhost', port=8081)
    await site.start()
    print("Server running on http://localhost:8081")

async def main():
    # Start server and client test concurrently
    server_task = asyncio.create_task(start_server())
    client_task = asyncio.create_task(test_client())
    await asyncio.gather(server_task, client_task)
      

asyncio.run(main())
