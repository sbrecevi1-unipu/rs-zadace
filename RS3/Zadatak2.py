import asyncio
import time
import json

'''
Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
se mora izvršavati ~5 sekundi.
'''
async def citaj_json(json_path):
    try:
        with open(json_path, "r", encoding="utf-8") as file:
            lista_proizvoljnih_rijecnika = json.load(file)
            return lista_proizvoljnih_rijecnika
    except FileNotFoundError:
        print(f"File not found: {json_path}")
        return None

async def korutina_korisnici():
    await asyncio.sleep(3)
    return await citaj_json("RS3/data/people_data.json")
  
    
async def korutina_proizvodi():
    await asyncio.sleep(5)
    return await citaj_json("RS3/data/product_data.json")

    
    
async def main():
    start_time = time.time()
    podaci_1, podaci_2 = await asyncio.gather(korutina_korisnici(), korutina_proizvodi())
    end_time = time.time()
    print(f'Podaci dohvaćeni. Korisnici: \n{podaci_1} , \n\n Proizvodi:\n{podaci_2}')
    time_difference = end_time - start_time
    print(f"Vrijeme trajanja: {time_difference:.0f} sekundi")
    
asyncio.run(main())