


'''
1. Definirajte korutinu fetch_users koja će slati GET zahtjev na JSONPlaceholder API na URL-u:
https://jsonplaceholder.typicode.com/users . Morate simulirate slanje 5 zahtjeva konkurentno
unutar main korutine. Unutar main korutine izmjerite vrijeme izvođenja programa, a rezultate
pohranite u listu odjedanput koristeći asyncio.gather funkciju. Nakon toga koristeći map funkcije ili
list comprehension izdvojite u zasebne 3 liste: samo imena korisnika, samo email adrese korisnika i
samo username korisnika. Na kraju main korutine ispišite sve 3 liste i vrijeme izvođenja programa.
'''


import asyncio
import aiohttp
import time

async def fetch_users(session):
    async with session.get('https://jsonplaceholder.typicode.com/users') as response:
        return await response.json()

async def main():
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users(session) for _ in range(5)]
        results = await asyncio.gather(*tasks)

    # Izvlačenje podataka u zasebne liste
    names = [user['name'] for user in results[0]]
    emails = [user['email'] for user in results[0]]
    usernames = [user['username'] for user in results[0]]

    # Ispis rezultata
    print("Imena korisnika:", names)
    print("Email adrese korisnika:", emails)
    print("Username korisnika:", usernames)
    print("Vrijeme izvođenja programa:", time.time() - start_time)

# Pokretanje glavne korutine
loop = asyncio.get_event_loop()
loop.run_until_complete(main())