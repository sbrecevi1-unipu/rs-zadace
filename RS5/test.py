from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp

async def get_users(request):
    return web.json_response({'korisnici': ['Ivo', 'Ana', 'Marko', 'Maja', 'Iva', 'Ivan']})

app = web.Application()

app.router.add_get('/korisnici', get_users)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")

async def main():
    await start_server() # Prvo pokreni poslužitelj
    async with aiohttp.ClientSession() as session: # Zatim otvori klijentsku sesiju
        rezultat = await session.get('http://localhost:8080/korisnici') # Pošalji GET zahtjev na lokalni poslužitelj
        print(await rezultat.text()) # Ispis odgovora
        while True:
            await asyncio.sleep(3600)  # Prevent the event loop from exiting

asyncio.run(main()) # Pokreni main korutinu