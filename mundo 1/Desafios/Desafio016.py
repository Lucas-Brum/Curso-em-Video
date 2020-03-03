from math import floor
numero = float(input('Digite um numero: '))
valor_inteiro = floor(numero)
print('O número \33[30m{}\33[m tem a parte inteira \33[1:45m{:.0f}\33[m'.format(numero, valor_inteiro))