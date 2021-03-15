print('-=' * 5, 'Gerador de PA Advance', '-=' * 5)
t1 = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
termo = t1
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{termo} - ', end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais?'))
print(f'Progressão finalizada com {total} termos mostrados')
