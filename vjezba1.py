# def kvadriraj(x):
    # return x ** 2
# lambda x: x**2

print('1.',(lambda x: x ** 2)(5)) # 25

# def zbroji_pa_kvadriraj(a, b):
#     return (a + b) ** 2
print('2.',(lambda x, y : (x + y)**2) (2,1))

# def kvadriraj_duljinu(niz):
#     return len(niz) ** 2
print('3.',(lambda niz: len(niz)**2)(['asdf',1234,1,'asdf2','p']))

# def pomnozi_i_potenciraj(x, y):
#     return (y * 5) ** x
print('4.',(lambda x,y: (y*5)**x)(2,2))

# def paran_broj(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return None
print('5.',(lambda x: True if x % 2==0 else None)(4)) # Ja bi rađe napisao True/False ili paran/neparan