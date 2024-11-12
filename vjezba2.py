def prijestupnost(godina):
    godina = int(godina)
    
    if (godina%4==0 and godina%100!=0) or (godina%400==0):
        rezultat = 'Godina ' + str(godina) + '. je prijestupna.'
    else:
        rezultat = 'Godina ' + str(godina) + '. nije prijestupna.'

    return rezultat

while True:
    sta = input('Upiši godinu ')
    print(prijestupnost(sta))