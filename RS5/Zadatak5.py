'''
Nadogradite poslužitelj iz prethodnog zadatka na način da podržava i POST metodu na putanji /narudzbe .
Ova ruta prima JSON podatke o novoj narudžbu u sljedećem obliku. Za početak predstavite da je svaka
narudžba jednostavna i sadrži samo jedan proizvod i naručenu količinu:

{
"proizvod_id": 1,
"kolicina": 2
}

Handler korutina ove metode mora provjeriti postoji li proizvod s traženim ID-em unutar liste proizvodi .
Ako ne postoji, vratite odgovor s statusom 404 i porukom {'error': 'Proizvod s traženim ID-em ne
postoji'} . Ako proizvod postoji, dodajte novu narudžbu u listu narudžbi i vratite odgovor s nadopunjenom
listom narudžbi u JSON formatu i prikladnim statusnim kodom.
Listu narudžbi definirajte globalno, kao praznu listu.
Vaš konačni poslužitelj mora sadržavati 3 rute: /proizvodi , /proizvodi/{id} i /narudzbe .
Testirajte poslužitelj na sve slučajeve kroz klijentsku sesiju unutar main korutine iste skripte.
'''

from aiohttp import web
import asyncio, aiohttp

import asyncio

narudzbe = []
test_narudzba= {
    "proizvod_id": 1,
    "kolicina": 2
    }
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
        
        # Unos narudzbe
        async with session.post('http://localhost:8081/narudzbe', json=test_narudzba) as resp:
            print('POST /narudzbe: ', await resp.json())
    
async def post_function(request):
    data = await request.json()
    proizvod_id = data.get('proizvod_id')
    matching_products = [p for p in proizvodi if p['id'] == proizvod_id]
    if not matching_products:  # This checks if the list is empty
        return web.json_response({'error': 'Proizvod s traženim ID-em ne postoji'}, status=404)
    else:
        narudzbe.append(data)

        return web.json_response(narudzbe)


app = web.Application()
app.router.add_get('/proizvodi', get_function)
app.router.add_get('/proizvodi/{id}', get_function_by_id)
app.router.add_post('/narudzbe', post_function)


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
