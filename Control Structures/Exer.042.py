r1 = int(input('Primeiro segmento:'))
r2 = int(input('Segundo segmento:'))
r3 = int(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Isósceles!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
else:
    print('Os segmentos acima não formam um triângulo!')