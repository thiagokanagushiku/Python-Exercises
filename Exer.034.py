Salario = float(input('Qual é o salário do funcionário? R$'))
if Salario >= 1250:
    Aumento = Salario*1.1
else:
    Aumento = Salario*1.15
print(f'Quem ganhava R${Salario:.2f} passa a ganhar R${Aumento:.2f} agora.')
