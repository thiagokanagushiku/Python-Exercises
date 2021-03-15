F = str(input('Digite uma frase:')).strip().lower()
print(f'A letra A aparece {F.count("a")} vezes na frase')
print(f'A primeira letra A apareceu na posição {F.find("a")+1}')
print(f'A última letra A apareceu na posição {F.rfind("a")+1}')


