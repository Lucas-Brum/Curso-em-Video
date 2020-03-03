velocidade = float(input('Velocidade do carro: '))
if velocidade > 80:
    print('\33[31mMultado em \33[34m{:.2f}\33[31mR$\33[m'.format((velocidade-80)*7))
print('\33[1:34mDirija com responsabilidade!!!')