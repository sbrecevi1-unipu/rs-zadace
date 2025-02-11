from aiohttp import web
import json
import hashlib

korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},
    {"korisnicko_ime": "markoMaric", "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"},
    {"korisnicko_ime": "Nada000", "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"}
]

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

async def register(request):
    data = await request.json()
    
    if 'korisnicko_ime' not in data or 'lozinka' not in data:
        return web.Response(status=400, text='Nedostaju podaci')
        
    # Provjera postoji li već korisnik
    if any(k['korisnicko_ime'] == data['korisnicko_ime'] for k in korisnici):
        return web.Response(status=409, text='Korisnik već postoji')
    
    novi_korisnik = {
        "korisnicko_ime": data['korisnicko_ime'],
        "lozinka_hash": hash_data(data['lozinka'])
    }
    korisnici.append(novi_korisnik)
    return web.Response(status=201, text='Korisnik uspješno registriran')

async def login(request):
    data = await request.json()
    
    if 'korisnicko_ime' not in data or 'lozinka' not in data:
        return web.Response(status=400, text='Nedostaju podaci')
    
    korisnik = next((k for k in korisnici if k['korisnicko_ime'] == data['korisnicko_ime']), None)
    
    if not korisnik:
        return web.Response(status=404, text='Korisnik ne postoji')
    
    if korisnik['lozinka_hash'] != hash_data(data['lozinka']):
        return web.Response(status=401, text='Pogrešna lozinka')
    
    return web.Response(text='Uspješna prijava')

app = web.Application()
app.router.add_post('/login', login)
app.router.add_post('/register', register)

if __name__ == '__main__':
    web.run_app(app, port=9000)