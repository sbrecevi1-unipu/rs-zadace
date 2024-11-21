
broj = int(input('\nUpiši broj za koji želiš faktorijel '))

rez=1
while broj > 0:
        
    rez *= broj
    broj -= 1
print('Sa while Loop-om: ' + str(rez))

# ili s for petljom
for broj in range(broj, 0):
    rez *= broj
    broj-=1
print('Sa for Loop-om: ' + str(rez) + '\n')