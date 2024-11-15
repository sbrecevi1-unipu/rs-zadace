

def brojanje_riječi(tekst):
    splitani = tekst.split(' ')
    broj_rijeci = {}
    for rijec in splitani:
        if rijec not in broj_rijeci:
            broj_rijeci[rijec] = splitani.count(rijec)
    return broj_rijeci
    
    # Ovo mi nije bilo orderano svaki put kako treba na outputu, ali čini mi se brže i kraće
    # splitani = tekst.split(' ')
    # return {jedinstvena_rijec: splitani.count(jedinstvena_rijec) for jedinstvena_rijec in set(splitani)}




# tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
tekst = input('...upiši mi nekakav tekst da ti riječi brojim...\n')
print(brojanje_riječi(tekst))

# sad radi kako treba:
# input = Nisam nikad bio, da sam bio, riječ izbrojio, ponekad , ali sad jesam! Samuel Brečević

# output = {'Nisam': 1, 'nikad': 1, 'bio,': 2, 'da': 1, 'sam': 1, 'riječ': 1, 'izbrojio,': 1, 'ponekad': 1, ',': 1, 'ali': 1, 'sad': 1, 'jesam!': 1, 'Samuel': 1, 'Brečević': 1}
