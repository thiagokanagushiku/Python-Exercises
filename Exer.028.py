from random import randint
from time import sleep
print('-='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-='*20)
N = int(input('Em que número eu pensei?'))
escolhido = randint(0, 5)
print('Processando...')
sleep(3)
if N == escolhido:
    print('PARABÉNS!!! Você conseguiu adivinhar minha mente!')
else:
    print(f'Não foi dessa vez! eu pensei no número {escolhido}!')





