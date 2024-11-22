print('1.')

import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")

# Stvaranje objekta klase Automobil
moj_automobil = Automobil("Volkswagen", "Golf", 2015, 120000)

# Pozivanje metoda
moj_automobil.ispis()
moj_automobil.starost()

############################################################################
print('###################################################################')
print('2.')

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Nije moguće dijeliti broj sa 0."
    
    def potenciranje(self):
        return self.a ** self.b
        
    def korijen(self):
        return self.a**0.5
    
objekt_kalkulatora= Kalkulator(5,3)

print("Zbroj:", objekt_kalkulatora.zbroj())
print("Oduzimanje:", objekt_kalkulatora.oduzimanje())
print("Množenje:", objekt_kalkulatora.mnozenje())
print("Dijeljenje:", objekt_kalkulatora.dijeljenje())
print("Potenciranje:", objekt_kalkulatora.potenciranje())
print("Korijen:", objekt_kalkulatora.korijen())

############################################################################
print('###################################################################')
print('3.')

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

# Lista studenata
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

# Stvaranje objekata klase Student
studenti_objekti = [Student(student["ime"], student["prezime"], student["godine"], student["ocjene"]) for student in studenti]

# Pronalaženje studenta s najvećim prosjekom
najbolji_student = max(studenti_objekti, key=lambda student: student.prosjek())

# Ispis informacija o najboljem studentu
print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime}, Prosjek: {najbolji_student.prosjek()}")

# u jednoj liniji:

# Ispis informacija o najboljem studentu u jednoj liniji 
print(f"Najbolji student: {(najbolji_student := max(studenti_objekti, key=lambda student: student.prosjek())).ime} {najbolji_student.prezime}, Prosjek: {najbolji_student.prosjek()}")

###############################################################################
print('###################################################################')
print('4.')
import math

class Krug:
    def __init__(self, r):
        self.r = r  # Radijus kruga

    def opseg(self):
        return 2 * math.pi * self.r  # Opseg kruga

    def povrsina(self):
        return math.pi * (self.r ** 2)  # Površina kruga

# Stvaranje objekta klase Krug s proizvoljnim radijusom
moj_krug = Krug(5)  # Primjer radijusa 5

# Ispis opsega i površine kruga
print(f"Opseg kruga: {moj_krug.opseg():.2f}")  # Ispis opsega s dvije decimale
print(f"Površina kruga: {moj_krug.povrsina():.2f}")  # Ispis površine s dvije decimale

print('###################################################################')
print('5.')

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)  # Pozivamo konstruktor roditeljske klase
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik, povecanje):
        if isinstance(povecanje, str):
            print('Sad ćemo malo karikirati povećanje plaća.')
            radnik.placa = str(radnik.placa) + ' + ' +  povecanje
        elif isinstance(povecanje, (int, float)):
            print('Znači ipak ćemo dignuti plaću...')
            radnik.placa += float(povecanje)
        else:
            print(f"Nevažeći tip za povećanje: {type(povecanje)}")

# Definiranje instance klase Radnik
radnik1 = Radnik("Samuel", "Sistem inženjer", 1000)

# Definiranje instance klase Manager
manager1 = Manager("Siniša", "Šef", 1500, "IT Odjel")

# Pozivanje metoda
radnik1.work()  # Ispisuje: Radim na poziciji Programer
manager1.work()  # Ispisuje: Radim na poziciji IT Menadžer u odjelu IT Odjel

# Povećanje plaće radnika od strane menadžera
print(f"Plaća prije povećanja: {radnik1.placa}")

manager1.give_raise(radnik1, 50)  # Povećavamo plaću radnika za, ah isto kikiriki
manager1.give_raise(radnik1, 'kikiriki')  # Povećavamo plaću radnika za kikiriki

print(f"Plaća nakon povećanja: {radnik1.placa}")

###########################################################################