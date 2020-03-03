from math import hypot
print('\33[1:41m-\33[m' * 50)
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
print('\33[1:41m-\33[m' * 50)
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
print('\33[1:41m-\33[m' * 50)
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print('A hipotenusa desse triangulo retangulo é \33[33m{}\33[m'.format(hipotenusa))