
# proizvodi.py

class Proizvod:
    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena}, Količina: {self.kolicina}")




proizvodi = [
    Proizvod("Slušalice", 20, 1),
    Proizvod("Grafička kartica", 100000, 1)
]
# Funkcija za dodavanje proizvoda u listu
def dodaj_proizvod(naziv, cijena, kolicina):
    novi_proizvod = Proizvod(naziv, cijena, kolicina)
    proizvodi.append(novi_proizvod)
