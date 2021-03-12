n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
opção = 0
while opção != 5:
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opção == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, 0 número {maior} é maior!')
    elif opção == 4:
        print('informe os valores novamente:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa.')