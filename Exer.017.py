from math import hypot
CO = float(input('comprimento do cateto oposto:'))
CA = float(input('comprimento do cateto adjacente:'))
print(f'A hipotenusa vai medir {hypot(CO, CA):.2f}')
