sexo = str(input('Informe seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Informe novamente seu sexo [M/F]:')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso!')
