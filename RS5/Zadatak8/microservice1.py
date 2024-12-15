'''
Definirajte 2 mikroservisa unutar direktorija cats .
Prvi mikroservis cat_microservice.py mora slušati na portu 8086 i na endpointu /cats vraćati JSON
odgovor s listom činjenica o mačkama. Endpoint /cat mora primati URL parametar amount koji
predstavlja broj činjenica koji će se dohvatiti. Na primjer, slanjem zahtjeva na /cat/30 dohvatit će se 30
činjenica o mačkama. Činjenice se moraju dohvaćati konkurentnim slanjem zahtjeva na CatFacts API.
Link: https://catfact.ninja/


U client.py pozovite ove dvije korutine sekvencijalno, obzirom da drugi mikroservis ovisi o rezultatima
prvog. Testirajte kod za proizvoljan broj činjenica.

'''

from aiohttp import web
import aiohttp
import asyncio

BASE_URL = "https://catfact.ninja/fact"


async def fetch_fact(session):
    """Fetch a single fact from CatFacts API."""
    async with session.get(BASE_URL) as response:
        if response.status == 200:
            data = await response.json()
            return data['fact']
        else:
            return None


async def fetch_facts(amount):
    """Fetch multiple facts concurrently."""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_fact(session) for _ in range(amount)]
        return await asyncio.gather(*tasks)


async def get_all_facts(request):
    """Return a general response with some default facts."""
    default_facts = [
        "Cats are fascinating creatures.",
        "Cats can sleep for 16 hours a day.",
        "Cats have retractable claws.",
    ]
    return web.json_response({"facts": default_facts})


async def get_facts_by_amount(request):
    """Fetch a specified number of cat facts."""
    amount = int(request.match_info['amount'])
    facts = await fetch_facts(amount)
    return web.json_response({"facts": facts})


app = web.Application()
app.router.add_get('/cats', get_all_facts)
app.router.add_get('/cat/{amount}', get_facts_by_amount)

if __name__ == '__main__':
    web.run_app(app, port=8086)

