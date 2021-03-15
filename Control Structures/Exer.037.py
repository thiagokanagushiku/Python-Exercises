n = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para Binário
[ 2 ] converter para Octal
[ 3 ] converter para Hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'{n} convertido para Binário é igual a {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para Octal é igual a {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para Hexadecimal é igual a {hex(n)[2:]}')
else:
    print('Opção inválida! Tente novamente.')
