distancia = float(input('Qual a distacia que sera percorrida? '))
if distancia <= 200:
    print('O valor a ser pago é de \33[31m{:.2f}R$'.format(distancia*0.5))
else:
    print('O valor a ser pago é de \33[34m{:.2f}R$'.format(distancia * 0.45))