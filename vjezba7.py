def verifikacija(poruka, lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        return 'Lozinka mora sadržavati između 8 i 15 znakova '
    elif not any(i.isupper() for i in lozinka) or not any(i.isdigit() for i in lozinka):
        return 'Lozinka mora sadržavati barem jedno veliko slovo i jedan broj\n'
    return 'Lozinka je ispravna'

neispravna = True
poruka = 'Upiši lozinku '
while neispravna:
    lozinka = input(poruka)
    poruka = verifikacija(poruka, lozinka)
    print(poruka)
    if poruka == 'Lozinka je ispravna':
        neispravna = False