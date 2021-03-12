from random import randint
comp = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
tentativa = 0
while not acertou:
    user = int(input('Qual é o seu palpite:'))
    tentativa += 1
    if user == comp:
        acertou = True
    else:
        if user > comp:
            print('Menos... Tente novamente!')
        elif user < comp:
            print('Mais... Tente novamente!')
print(f'\33[34mAcertou com {tentativa} tentativas!\33[m')
