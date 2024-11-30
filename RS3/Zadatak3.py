import asyncio
import time
import json

'''
3. Definirajte korutinu autentifikacija() koja će simulirati autentifikaciju korisnika na
poslužiteljskoj strani. Korutina kao ulazni parametar prima rječnik koji opisuje korisnika, a sastoji se
od ključeva korisnicko_ime , email i lozinka . Unutar korutine simulirajte provjeru korisničkog
imena na način da ćete provjeriti nalaze li se par korisnicko_ime i email u bazi korisnika. Ova
provjera traje 3 sekunde.
'''

baza_korisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def autorizacija(korisnik, unesena_lozinka):
    await asyncio.sleep(2)  # Simulate decryption process
    for entry in baza_lozinka:
        if entry['korisnicko_ime'] == korisnik['korisnicko_ime']:
            if entry['lozinka'] == unesena_lozinka:
                result =  f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija uspješna."
            else:
                result =  f"Korisnik {korisnik['korisnicko_ime']}: Autorizacija neuspješna."
            
    return result

async def autentifikacija(korisnik):
    await asyncio.sleep(3)
    for korisnik_iz_baze in baza_korisnika:
        if korisnik_iz_baze["korisnicko_ime"] == korisnik["korisnicko_ime"] and korisnik_iz_baze["email"] == korisnik["email"]:
            print(await autorizacija(korisnik_iz_baze, korisnik['lozinka']))
            return f"Korisnik {korisnik['korisnicko_ime']} je pronađen."  
        else:
            return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."  
    
 
async def main():
    korisnik = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    rezultat = await autentifikacija(korisnik)
    print(rezultat)



asyncio.run(main())