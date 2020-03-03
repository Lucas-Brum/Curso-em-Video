print('Convesor de \33[1:47mReais\33[m em \33[1:44mDollar\33[m')
print('Cotação atual = 4,28')
dinheiro = float(input('Digite o valor a ser convertido = R$ '))
print('\33[1:37m{:.2f}\33[m Em R$ vale \33[1:34m{:.2f}\33[m em US$'.format(dinheiro, dinheiro / 4.28))