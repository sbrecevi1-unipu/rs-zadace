def kalkulator(var1, var2, operacija):
    var1 = float(var1)
    var2 = float(var2)
    # print(type(var1),type(var2))
    if operacija == '+':
        rezultat = var1+var2
    elif operacija == '-':
        rezultat = var1-var2
    elif operacija == '*' :
        rezultat = var1*var2
    elif operacija=='/':
        rezultat = var1/var2

    return 'Rezultat operacije ' + str(var1) + ' ' + str(operacija) + ' '  + str(var2) + ' je ' + str(rezultat)

while True:
    sta = input('Upiši prvi broj, drugi broj i željenu operaciju odvojeno zarezom (2,5,*)')
    arguments = sta.split(',')
    print(kalkulator(arguments[0], arguments[1], arguments[2]))