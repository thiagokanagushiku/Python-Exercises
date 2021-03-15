D = float(input('Qual é a distância da sua viagem?'))
print(f'Você está prestes a começar uma viagem de {D:.1f}Km')
if D > 200:
    print(f'E o preço da sua passagem será de R${D*0.45:.2f}')
else:
    print(f'E o preço da sua passagem será de R${D*0.50:.2f}')
