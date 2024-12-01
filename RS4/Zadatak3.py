'''
Definirajte korutinu get_dog_fact koja dohvaća činjenice o psima sa DOG API.
Korutina get_dog_fact neka dohvaća činjenicu o psima na URL-u: https://dogapi.dog/api/v2/facts .
Nakon toga, definirajte korutinu get_cat_fact koja dohvaća činjenicu o mačkama slanjem zahtjeva na
URL: https://catfact.ninja/fact .
Istovremeno pohranite rezultate izvršavanja ovih Taskova koristeći asyncio.gather(*dog_facts_tasks,
*cat_facts_tasks) funkciju u listu dog_cat_facts , a zatim ih koristeći list slicing odvojite u dvije liste
obzirom da znate da je prvih 5 činjenica o psima, a drugih 5 o mačkama.
Na kraju, definirajte i treću korutinu mix_facts koja prima liste dog_facts i cat_facts i vraća novu
listu koja za vrijednost indeksa i sadrži činjenicu o psima ako je duljina činjenice o psima veća od duljine
činjenice o mačkama na istom indeksu, inače vraća činjenicu o mački. Na kraju ispišite rezultate filtriranog
niza činjenica. Liste možete paralelno iterirati koristeći zip funkciju, npr. for dog_fact, cat_fact in
zip(dog_facts, cat_facts) .

'''


import asyncio
import aiohttp

# Korutina za dohvaćanje činjenica o psima
async def get_dog_fact():
    url = "https://dogapi.dog/api/v2/facts"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("data")[0].get("attributes").get("body")  # Dohvati činjenicu
            else:
                return None

# Korutina za dohvaćanje činjenica o mačkama
async def get_cat_fact():
    url = "https://catfact.ninja/fact"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("fact")  # Dohvati činjenicu
            else:
                return None

# Korutina za miješanje činjenica o psima i mačkama
async def mix_facts(dog_facts, cat_facts):
    mixed_facts = [
        dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
        for dog_fact, cat_fact in zip(dog_facts, cat_facts)
    ]
    return mixed_facts

# Glavna korutina
async def main():
    # Kreiranje Taskova za dohvaćanje 5 činjenica o psima i mačkama
    dog_facts_tasks = [asyncio.create_task(get_dog_fact()) for _ in range(5)]
    cat_facts_tasks = [asyncio.create_task(get_cat_fact()) for _ in range(5)]

    # Paralelno izvršavanje Taskova
    dog_cat_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

    # Razdvajanje činjenica u dvije liste
    dog_facts = dog_cat_facts[:5]
    cat_facts = dog_cat_facts[5:]

    # Filtriranje praznih činjenica
    dog_facts = [fact for fact in dog_facts if fact]
    cat_facts = [fact for fact in cat_facts if fact]

    # Miješanje činjenica o psima i mačkama
    mixed_facts = await mix_facts(dog_facts, cat_facts)

    # Ispis rezultata
    print("Dog Facts:")
    for fact in dog_facts:
        print(fact)

    print("\nCat Facts:")
    for fact in cat_facts:
        print(fact)

    print("\nMixed Facts:")
    for fact in mixed_facts:
        print(fact)

# Pokreni program
if __name__ == "__main__":
    asyncio.run(main())
