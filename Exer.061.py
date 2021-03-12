print('-=' * 5, 'Gerador de PA', '-=' * 5)
t1 = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = t1
c = 1
while c <= 10:
    print(f'{termo} - ', end='')
    termo += razao
    c += 1
print('FIM')