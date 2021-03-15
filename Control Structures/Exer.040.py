n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
média = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {média:.1f}')
if média >= 7:
    print('\33[34mO aluno está APROVADO\33[m' )
elif 7 > média >= 5:
    print('Você está de RECUPERAÇÂO!')
elif média < 5 :
    print('\33[31mO aluno está REPROVADO!\33[m')
