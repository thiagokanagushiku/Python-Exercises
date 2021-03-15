from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
comp = randint(0,2)
print('''Sua opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
user = int(input('Faça sua jogada:'))
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO')
print('-=' * 18)
print(f'O computador escolheu {itens[comp]}!')
if comp == 0:
    if user == 0:
        print('Empate!!!')
    elif user == 1:
        print('Você ganhou!!!')
    elif user == 2:
        print('\33[1:31mVocê PERDEU!!!\33[m')
elif comp == 1:
    if user == 0:
        print('\33[1:31mVocê PERDEU!!!\33[m')
    elif user == 1:
        print('Empate!!!')
    elif user == 2:
        print('Você ganhou!!!')
elif comp == 2:
    if user == 0:
        print('Você ganhou!!!')
    elif user == 1:
        print('\33[1:31mVocê PERDEU!!!\33[m')
    elif user ==2:
        print('Empate!!!')
print('-=' * 18)
