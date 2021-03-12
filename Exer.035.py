print('\033[31m-=\033[m'*20)
print('Analisador de Triângulos')
print('\033[31m-=\033[m'*20)
PS = float(input('Primeiro segmento:'))
SS = float(input('Segundo segmento:'))
TS = float(input('Terceiro segmento'))
if PS < (SS + TS) and SS < (PS + TS) and TS < (PS + SS):
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')