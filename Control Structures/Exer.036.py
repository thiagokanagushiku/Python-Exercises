casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
prestação = casa / (anos * 12)
minimo = salario * 0.3
print(f'Para pagar uma casa de {casa:.2f} em {anos} anos a prestação será de {prestação:.2f}')
print(f'A prestação será de {prestação}')
if prestação <= minimo:
    print('\33[34mEmprestimo ACEITO!\33[m')
else:
    print('\33[31mEmprestimo NEGADO!\33[m')
