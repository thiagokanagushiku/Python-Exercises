Nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúscula é {Nome.upper()}')
print(f'Seu nome em minúscula é {Nome.lower()}')
print(f'Seu nome tem ao todo {len(Nome) - Nome.count(" ")} letras')
separa = Nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')











