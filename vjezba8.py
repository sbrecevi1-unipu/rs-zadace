def oddpop(niz):
    for i in niz:
        if int(i)%2!=0:
            niz.pop(niz.index(i))
    return niz


niz= input('Upiši niz iz kojeg želiš da izbacim neparne brojeve. npr. 1,2,3,4,5,6\n').split(',')
niz = [int(i) for i in niz]

print(oddpop(niz))