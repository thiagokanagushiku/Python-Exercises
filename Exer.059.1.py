v1 = int(input('Primeiro valor:'))
v2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('[ 1 ] Somar'
          '[ 2 ] Multiplicar'
          '[ 3 ] Maior '
          '[ 4 ] Novos números'
          '[ 5 ] Sair do programa')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        print(f'A soma de {v1} e {v2} é igual a {v1 + v2}')
    elif opção == 2:
        print(f'O produto de {v1} x {v2} é {v1 * v2}')
    elif opção == 3:
        if v1 > v2:
            print(f'Comparando {v1} e {v2} o maior é {v1}')
        else:
            print(f'Comparando {v1} e {v2} o maior é {v2} ')
    elif opção == 4:
         v1 = int(input('Primeiro valor:'))
         v2 = int(input('Segundo valor:'))
    print('\33[34mー＝\33[m' * 20)
print('Fim do programa')