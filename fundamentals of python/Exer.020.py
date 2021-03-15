from random import shuffle
P = input('Primeiro aluno:')
S = input('Segundo alunos:')
T = input('Terceiro aluno:')
Q = input('Quarto aluno:')
lista = [P, S, T, Q]
ordem = shuffle(lista)
print('A ordem de apresentação será')
print(lista)

