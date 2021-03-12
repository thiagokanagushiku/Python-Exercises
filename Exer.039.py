from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento:'))
idade = (atual - ano)
restante = 18 - idade
print(f'Quem nasceu em {ano} tem {atual - ano} em 2020')
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos!')
    print(f'Seu alistamento foi em {ano + 18}')
elif idade < 18:
    print(f'Ainda faltam {restante} anos para o alistamento!')
    print(f'Seu alistamento será em {ano + 18}!')
else:
    print('Você tem que se alistar imediatamente')
