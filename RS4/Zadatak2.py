

'''
2. Definirajte dvije korutine, od kojih će jedna služiti za dohvaćanje činjenica o mačkama koristeći
get_cat_fact korutinu koja šalje GET zahtjev na URL: https://catfact.ninja/fact . Izradite 20
Task objekata za dohvaćanje činjenica o mačkama te ih pozovite unutar main korutine i rezultate
pohranite odjednom koristeći asyncio.gather funkciju. Druga korutina filter_cat_facts ne šalje
HTTP zahtjeve, već mora primiti gotovu listu činjenica o mačkama i vratiti novu listu koja sadrži samo
one činjenice koje sadrže riječ "cat" ili "cats" (neovisno o velikim/malim slovima).
'''
import asyncio
import aiohttp

# Korutina za dohvaćanje činjenica o mačkama
async def get_cat_fact():
    url = "https://catfact.ninja/fact"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("fact")
            else:
                return None

# Korutina za filtriranje činjenica o mačkama
async def filter_cat_facts(cat_facts):
    return [fact for fact in cat_facts if "cat" in fact.lower() or "cats" in fact.lower()]

# Glavna korutina
async def main():
    # Kreiraj 20 Task objekata za dohvaćanje činjenica o mačkama
    try:
        tasks = [asyncio.create_task(get_cat_fact()) for _ in range(20)]
    except: 
        print('Somekind of error')
    # Čekaj rezultate svih Task objekata
    facts = await asyncio.gather(*tasks)
    
    # Filtriraj činjenice koje su None
    facts = [fact for fact in facts if fact is not None]
    
    # Filtriraj činjenice koje sadrže "cat" ili "cats"
    filtered_facts = await filter_cat_facts(facts)
    
    # Ispis rezultata
    print("Original facts:")
    for fact in facts:
        print(fact)
    
    print("\nFiltered facts:")
    for fact in filtered_facts:
        print(fact)


asyncio.run(main())


