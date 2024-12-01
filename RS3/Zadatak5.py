import asyncio
import time
import json
import random

'''
5. Definirajte korutinu secure_data koja će simulirati enkripciju osjetljivih podataka. Kako se u
praksi enkripcija radi na poslužiteljskoj strani, korutina će simulirati enkripciju podataka u trajanju od 3
sekunde. Korutina prima kao argument rječnik osjetljivih podataka koji se sastoji od ključeva prezime ,
broj_kartice i CVV . Definirajte listu s 3 rječnika osjetljivih podataka. Pohranite u listu zadaci kao u
prethodnom zadatku te pozovite zadatke koristeći asyncio.gather() . Korutina secure_data mora za
svaki rječnik vratiti novi rječnik u obliku: {'prezime': prezime , 'broj_kartice': 'enkriptirano',
'CVV': 'enkriptirano'} . Za fake enkripciju koristite funkciju hash(str) koja samo vraća hash
vrijednost ulaznog stringa.
'''




async def secure_data(osjetljivi_podaci):
    await asyncio.sleep(3)  # Simulacija trajanja enkripcije
    return {
        'prezime': osjetljivi_podaci['prezime'],
        'broj_kartice': hash(osjetljivi_podaci['broj_kartice']),
        'CVV': hash(osjetljivi_podaci['CVV'])
    }

zadaci = [
    {'prezime': 'Horvat', 'broj_kartice': '1234-5678-9876-5432', 'CVV': '123'},
    {'prezime': 'Ivić', 'broj_kartice': '2345-6789-8765-4321', 'CVV': '456'},
    {'prezime': 'Kovač', 'broj_kartice': '3456-7890-7654-3210', 'CVV': '789'}
]
    
    
 
async def main():
    
    start_time = time.time()
    print(await asyncio.gather(*(secure_data(zadatak) for zadatak in zadaci)))
    end_time = time.time()
    time_difference = end_time - start_time
    print(f"Završeno u {time_difference : .0f} sekunde/i")

asyncio.run(main())