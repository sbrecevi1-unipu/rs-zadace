'''
Unutar client.py datoteke definirajte 1 korutinu koja može slati zahtjev na oba mikroservisa, mora
primati argumente url i port . Korutina neka vraća JSON odgovor.
Korutinu pozovite unutar main korutine. Prvo demonstrirajte sekvencijalno slanje zahtjeva, a zatim
konkurentno slanje zahtjeva.
'''

import aiohttp
import asyncio
import time


async def fetch_service1():
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://localhost:8081/pozdrav')
        return await response.json()
async def fetch_service2():
    async with aiohttp.ClientSession() as session:
        response = await session.get('http://localhost:8082/pozdrav')
        return await response.json()

async def main():
    ####Sekvencijalno - trebalo bi biti how_much + how_much sec####
    start = time.time()
    print("Pokrećem sekvencijalno korutine")
    service1_response = await fetch_service1()
    print(f"Odgovor mikroservisa 1: {service1_response}")
    service2_response = await fetch_service2()
    print(f"Odgovor mikroservisa 2: {service2_response}")
    end = time.time()
    print(f"Izvršavanje je trajalo {end - start:.2f} sekundi.")
    ##AS iT should be: Izvršavanje je trajalo 7.03 sekundi.
    ####Konkurentno - trebalo bi biti how_much koji je veći
    start = time.time()
    print("That sums it up!\n\nPokrećem konkurentno korutine")
    results = await asyncio.gather(fetch_service1(), fetch_service2()) # konkurentno slanje zahtjeva, vraća listu rječnika
    ##ispis jednak gornjem
    for _ in results:
        print(f"Odgovor mikroservisa {results.index(_)+1}: {_}")
    end = time.time()
    print(f"Izvršavanje je trajalo {end - start:.2f} sekundi.")
    ###########################################################
asyncio.run(main())

