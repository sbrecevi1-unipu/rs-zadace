def ukloni_duplikate(lista):
    lista=set(lista)
    return(lista)

lista= input('Upiši niz iz kojeg želiš da izbacim neparne brojeve. npr. 1,2,3,4,5,6\n').split(',')
lista = [int(i) for i in lista]

print(ukloni_duplikate(lista))