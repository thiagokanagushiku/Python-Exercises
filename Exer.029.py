V = float(input('Qual é a velocidade atual do carro?'))
if V > 80:
    print('Multado! você excedeu o limite que é de 80km/h')
    print(f'Você deve pagar uma multa de R${(V - 80)*7:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')
