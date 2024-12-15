
import aiohttp
import asyncio
import time


async def zbroj():
    async with aiohttp.ClientSession() as session:
        data_json = {
            'podaci': [0,0,0,0]
        }
        response = await session.post('http://localhost:8083/zbroj', json=data_json)
        return await response.json()

async def umnozak():
    async with aiohttp.ClientSession() as session:
        data_json = {
            'podaci': [1,2,3,4,5,6,7,8,9]
        }
        response = await session.post('http://localhost:8084/umnozak', json=data_json)
        return await response.json()

async def djeljenje(umnozak,zbroj):
    async with aiohttp.ClientSession() as session:
        data_json = {
            'podaci': [umnozak, zbroj]
        }
        response = await session.post('http://localhost:8085/kolicnik', json = data_json)
        print(response.status)
        return await response.json()


async def main():
    start = time.time()
    # print("That sums it up!\n\nPokrećem konkurentno korutine")
    # service1_response = await zbroj()
    # service2_response = await umnozak()
    
    results = await asyncio.gather(zbroj(), umnozak()) # konkurentno slanje zahtjeva, vraća listu rječnika
    
    
    for _ in results:
        print(f"Odgovor mikroservisa {results.index(_)+1}: {_}")
        if results.index(_)+1 == 1:
            zbroj1=_
        elif results.index(_)+1 == 2:
            umnozak1=_
    end = time.time()
    print(f"Izvršavanje je trajalo {end - start:.2f} sekundi.")

    print(f"Pozivam djeljenje")
    
    ## pozovi mi funkciju djeljenje ali bez asyncio.gather
    start = time.time()
    # djeljenje_response = await djeljenje(umnozak1,zbroj1)
    print(await djeljenje(umnozak1,zbroj1))














    ###########################################################

asyncio.run(main())
