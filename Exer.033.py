PV = int(input('Primeiro valor:'))
SV = int(input('Segundo valor:'))
TV = int(input('Terceiro valor:'))
menor = PV
if SV < PV and SV < TV:
    menor = SV
if TV < PV and TV < SV:
    menor = TV
maior = PV
if SV > PV and SV > TV:
    maior = SV
if TV > PV and TV > SV:
    maior = TV

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')

