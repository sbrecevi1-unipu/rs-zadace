
from shop.proizvodi import proizvodi as lista_proizvoda, dodaj_proizvod
from shop.narudzbe import napravi_narudzbu, narudzbe

# Lista proizvoda
proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 2},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 1},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 1},
    {"naziv": "Miš", "cijena": 100, "kolicina": 1}
    
]

# Dodajemo proizvode u listu
for proizvod in lista_proizvoda:
    dodaj_proizvod(proizvod.naziv, proizvod.cijena, proizvod.kolicina)

# Napravimo narudžbu
nova_narudzba = napravi_narudzbu(proizvodi)

# Ispisujemo narudžbu ako je uspješno napravljena
if nova_narudzba:
    nova_narudzba.ispis_narudzbe()