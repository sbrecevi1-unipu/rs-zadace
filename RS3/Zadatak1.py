import asyncio
import time

async def dohvati_podatke():
    await asyncio.sleep(3)
    lista_brojeva = [x for x in range(0,11)]
    return lista_brojeva
async def main():
    start_time = time.time()
    podaci = await dohvati_podatke()
    end_time = time.time()
    print(f'Podaci dohvaćeni. {podaci}')
    time_difference = end_time - start_time
    print(f"Vrijeme trajanja: {time_difference:.0f} sekundi")
    
asyncio.run(main())
