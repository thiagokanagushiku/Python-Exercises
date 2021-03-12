from random import randint
comp = randint(0, 10)
print(comp)
print('ー＝'*5,'\33[32mゲームタイム\33[m','ー＝'* 5)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
c = 0
while not acertou:
    user = int(input('Digite seu palpite:'))
    if comp == user:
        acertou = True
    else:
        acertou = False
        if comp > user:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
    c += 1
print(f'Acertou em {c} tentativas!')
