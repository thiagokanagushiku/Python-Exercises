from datetime import date
A = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
if A == 0:
    A = date.today().year
if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
    print (f'O ano {A} é bissexto!')
else:
    print(f'O ano {A} não é bissexto!')
