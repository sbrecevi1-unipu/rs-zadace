'''
Treći mikroservis pozovite nakon konkurentnog izvršavanja prvog i drugog mikroservisa. Dakle treći ide
sekvencijalno jer mora čekati rezultati prethodna 2. Ovaj mikroservis neka sluša na portu 8085 te na
endpointu /kolicnik očekuje JSON s podacima prva dva servisa. Kao odgovor mora vratiti količnik
umnoška i zbroja.
'''

from aiohttp import web


async def djeljenje(request):
    
        
    data = await request.json()
    umnozak = data['podaci'][0]['umnozak']
    zbroj = data['podaci'][1]['zbroj']
    if zbroj == 0 :
        return web.json_response({'error': 'Nije moguće izvršiti djeliti s nulom'}, status = 405)
    kolicnik = {'kolicnik' : umnozak/zbroj}
    

    return web.json_response(kolicnik, status = 200)
    


    


app = web.Application()
app.router.add_post('/kolicnik', djeljenje)



if __name__ == '__main__':
    web.run_app(app, port=8085)

