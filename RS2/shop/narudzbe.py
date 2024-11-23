
from shop.proizvodi import proizvodi  # Importiramo listu proizvoda

# Lista za pohranu narudžbi
narudzbe = []

class Narudzba:
    def __init__(self, proizvodi, ukupna_cijena):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        proizvodi_ispis = ', '.join(f"{proizvod['naziv']} x {proizvod['kolicina']}" for proizvod in self.proizvodi)
        print(f"Naručeni proizvodi: {proizvodi_ispis}, Ukupna cijena: {self.ukupna_cijena} eur")

def napravi_narudzbu(proizvodi):
    # Provjera uvjeta
    if not isinstance(proizvodi, list):
        print("Argument proizvodi mora biti lista.")
        return None
    if not proizvodi:
        print("Lista ne smije biti prazna.")
        return None
    for proizvod in proizvodi:
        if not isinstance(proizvod, dict):
            print("Svaki element u listi mora biti rječnik.")
            return None
        if not all(key in proizvod for key in ["naziv", "cijena", "kolicina"]):
            print("Svaki rječnik mora sadržavati ključeve naziv, cijena i kolicina.")
            return None

    # Provjera dostupnosti proizvoda
    ukupna_cijena = sum(proizvod["cijena"] * proizvod["kolicina"] for proizvod in proizvodi)
    for proizvod in proizvodi:
        dostupno = next((p for p in proizvodi if p["naziv"] == proizvod["naziv"]), None)
        if not dostupno or dostupno["kolicina"] < proizvod["kolicina"]:
            print(f"Proizvod {proizvod['naziv']} nije dostupan!")
            return None

    # Stvaranje nove narudžbe
    nova_narudzba = Narudzba(proizvodi, ukupna_cijena)
    narudzbe.append(nova_narudzba)
    return nova_narudzba