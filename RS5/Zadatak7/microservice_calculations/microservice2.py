'''
Drugi mikroservis neka sluša na portu 8084 te kao ulazni podataka prima iste podatke. Na endpointu
/umnozak neka vraća JSON odgovor s umnoškom svih brojeva. Dodajte provjeru ako brojevi nisu
proslijeđeni, vratite odgovarajući HTTP odgovor i statusni kod.
'''



from aiohttp import web



async def umnozak(request):
    try:
        umnozak = 1
        data = await request.json()
        for _ in data['podaci']:
            umnozak *= _ 
        umnozak_dict = {
            'umnozak' : umnozak
        }
        return web.json_response(umnozak_dict, status = 200)
    except:
        return web.json_response('Method Not Allowed', status = 405)
        pass
    




app = web.Application()
app.router.add_post('/umnozak', umnozak)


if __name__ == "__main__":
    web.run_app(app, port=8084)
