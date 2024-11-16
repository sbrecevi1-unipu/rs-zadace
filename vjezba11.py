

def grupiraj_po_paritetu(lista):
    rjecnik = {}
    rjecnik['parni']   = []
    rjecnik['neparni'] = []

    for i in lista:
        if i % 2 == 0:
            rjecnik['parni'].append(i)
        else:
            rjecnik['neparni'].append(i)
    return rjecnik
    

lista = input('...upiši mi niz brojeva da sortiram parne i neparne... npr 1,2,3,4\n').split(',')
lista = [int(i) for i in lista]
print(grupiraj_po_paritetu(lista))
