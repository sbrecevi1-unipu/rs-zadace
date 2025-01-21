'''
U client.py pozovite ove dvije korutine sekvencijalno, obzirom da drugi mikroservis ovisi o rezultatima
prvog. Testirajte kod za proizvoljan broj činjenica.
'''


import aiohttp
import asyncio


async def get_facts(amount):
    """Fetch facts from the first microservice."""
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://localhost:8086/cat/{amount}') as response:
            if response.status == 200:
                data = await response.json()
                return data['facts']
            else:
                print(f"Error fetching facts: {response.status}")
                return []


async def check_facts(facts):
    """Send facts to the second microservice for checking."""
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8087/facts', json={"facts": facts}) as response:
            if response.status == 200:
                data = await response.json()
                return data['filtered_facts']
            else:
                print(f"Error checking facts: {response.status}")
                return []


async def main():
    amount = 10
    print("Dohvaćanje s prvog mikroservisa")
    facts = await get_facts(amount)
    print(f"Dohvaćeno {len(facts)} činjenica.")

    print("Šaljem činjenice 2. mikroservisu")
    filtered_facts = await check_facts(facts)
    print(f"Filtrirane činjenice: {filtered_facts}")

if __name__ == '__main__':
    asyncio.run(main())    