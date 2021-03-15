P = float(input('Qual é o seu peso? (kg)'))
A = float(input('Qual é a sua altura? (m)'))
imc = P / (A ** 2)
print(f'O IMC dessa pessoa é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO do peso!')
elif 25 > imc >= 18.5:
    print('Você está no seu peso IDEAL!')
elif 30 > imc >= 25:
    print('Você está com SOBREPESO!')
elif 40 > imc >= 30:
    print('Você está com OBESIDADE')
else:
    print('VocÊ está com OBESIDADE MÓRBIDA!')

