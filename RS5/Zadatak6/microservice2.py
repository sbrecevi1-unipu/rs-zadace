'''
Definirajte 2 mikroservisa u 2 različite datoteke. 
Prvi mikroservis neka sluša na portu 8081 i na endpointu
/pozdrav vraća JSON odgovor nakon 3 sekunde čekanja, 
u formatu: {"message": "Pozdrav nakon 3 sekunde"} . 
Drugi mikroservis neka sluša na portu 8082 te na istom 
endpointu vraća JSON odgovor nakon 4 sekunde: 
{"message": "Pozdrav nakon 4 sekunde"} . 
Unutar client.py datoteke definirajte 1 korutinu koja može 
slati zahtjev na oba mikroservisa, mora primati argumente url
i port . Korutina neka vraća JSON odgovor.
Korutinu pozovite unutar main korutine. 
Prvo demonstrirajte sekvencijalno slanje zahtjeva, a zatim
konkurentno slanje zahtjeva.
'''

from aiohttp import web
import asyncio
how_much = 4
async def handler_function(request): 
    await asyncio.sleep(how_much)
    return web.json_response({"message": f"Pozdrav nakon {how_much} sekunde"}, status = 200)


app = web.Application()
app.router.add_get('/pozdrav', handler_function)
if __name__ == "__main__":

    web.run_app(app, port=8082)