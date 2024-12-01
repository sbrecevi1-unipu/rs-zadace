import asyncio
import time
import json
import random

'''
4. Definirajte korutinu provjeri_parnost koja će simulirati "super zahtjevnu operaciju" provjere
parnosti broja putem vanjskog API-ja. Korutina prima kao argument broj za koji treba provjeriti
parnost, a vraća poruku "Broj {broj} je paran." ili "Broj {broj} je neparan." nakon 2 sekunde.
Unutar main funkcije definirajte listu 10 nasumičnih brojeva u rasponu od 1 do 100 (koristite random
modul). Listu brojeva izgradite kroz list comprehension sintaksu. Nakon toga, pohranite u listu zadaci
10 Task objekata koji će izvršavati korutinu provjeri_parnost za svaki broj iz liste (također kroz list
comprehension). Na kraju, koristeći asyncio.gather() , pokrenite sve korutine konkurentno i ispišite
rezultate.
'''




async def provjeri_parnost(broj):
    await asyncio.sleep(2)  # Simulate decryption process
    
    if broj % 2 == 0:
        result =  f"Broj {broj} je paran."
    else:
        result =  f"Broj {broj} je neparan."
            
    return result



    
 
async def main():
    
    start_time = time.time()
    
    lista_brojeva = [random.randint(1, 100)  for x in range(10)]
    zadaci = [asyncio.create_task(provjeri_parnost(x)) for x in lista_brojeva]
    print(await asyncio.gather(* zadaci))
    
    end_time = time.time()
    time_difference = end_time - start_time
    print(f"Završeno u {time_difference : .0f} sekunde/i")

asyncio.run(main())