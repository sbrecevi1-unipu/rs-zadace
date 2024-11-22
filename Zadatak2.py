nizovi = ["jabuka", "kruška", "banana", "naranča"]

kvadrirane_duljine = lambda x: len(x)**2

print('1.', list(map(kvadrirane_duljine, nizovi))) # [36, 36, 36, 49]

#######################################################################

brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

veci_od_5 = lambda x: x > 5

print('2.', list(filter(veci_od_5, brojevi))) # [21, 33, 45, 9, 10]

######################################################################

brojevi = [10, 5, 12, 15, 20]

transform = lambda x: (x, x**2) # Moram priznati... MOĆNO. Nikad koristio

print('3.', dict(map(transform, brojevi))) # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}

# transform = dict(map(lambda x: (x, x**2), brojevi))
# print(transform) # Ovako mi se čak čini jasnije

#####################################################################

studenti = [
        {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
        {"ime": "Marko", "prezime": "Marković", "godine": 22},
        {"ime": "Ana", "prezime": "Anić", "godine": 21},
        {"ime": "Petra", "prezime": "Petrić", "godine": 13},
        {"ime": "Iva", "prezime": "Ivić", "godine": 17},
        {"ime": "Mate", "prezime": "Matić", "godine": 18}
        ]
svi_punoljetni = all(map (lambda x: x["godine"] >= 18, studenti))
print('4.', svi_punoljetni) # False

#####################################################################

# Definirajte varijablu min_duljina koja će pohranjivati int . Koristeći odgovarajuću funkciju višeg reda
# i lambda izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od
# min_duljina :

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]
min_duljina = input("Unesite minimalnu duljinu riječi: ")
# min_duljina = 7
duge_rijeci = list(filter(lambda x: len(x) >= int(min_duljina), rijeci))
print(duge_rijeci)
# print(duge_rijeci) # ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']