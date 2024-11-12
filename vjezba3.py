import random

broj = random.randrange(1,100)
pokusaji=0
broj_je_pogoden=False

while broj_je_pogoden==False:
    # print('random broj je ' + str(broj))
    sta = int(input('Upiši broj (od 1 do 100) \n'))
    if sta>broj:
        pokusaji+=1
        print('Broj je manji\n')
    elif sta<broj:
        pokusaji+=1
        print('Broj je veći\n')
    elif sta==broj:
        pokusaji+=1
        broj_je_pogoden=True

print('Bravo, pogodio si u ' + str(pokusaji) + ' pokušaja.')
