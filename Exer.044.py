print('=' * 20, 'チアゴ店', '=' * 20)
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção'))
if opção == 1:
    total = preço * 0.9
elif opção == 2:
    total = preço * 0.95
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${preço / 2:.2f} SEM JUROS!')
elif opção == 4:
    total = preço * 1.2
    totalparcelas = int(input('Quantas parcelas?'))
    parcela = total / totalparcelas
    print(f'Sua compra será parcelada em {totalparcelas}x de R${parcela:.2f} COM JUROS!')
else:
    total = preço
    print('Opção invalida. Tente novamente!')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final!')
