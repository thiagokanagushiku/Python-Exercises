from random import choice
P = input('Primeiro aluno:')
S = input('Segundo aluno:')
T = input('Terceiro aluno:')
Q = input('Quarto aluno')
Lista = [P, S, T, Q]
print(f'O aluno escolhido foi {choice(Lista)}')


