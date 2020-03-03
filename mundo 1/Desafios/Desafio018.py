import math
angulo = float(input('Digite um angulo: '))
seno =math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente =math.tan(math.radians(angulo))
print('O seno do numero é \33[31m{:.2f}\33[m'.format(seno))
print('O cosseno do numero é \33[31m{:.2f}\33[m'.format(cosseno))
print('A tangente do numero é \33[31m{:.2f}\33[m'.format(tangente))
