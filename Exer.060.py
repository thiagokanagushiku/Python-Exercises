n = int(input('calcular seu fatorial:'))
print(f'calculando {n}! = ', end='')
c = n
f = 1
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)


