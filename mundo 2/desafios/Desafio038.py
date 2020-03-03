print('\33[31m-=-\33[m' * 20)
print('\33[4m\33[1mQual valor é maior?')
print('\33[m\33[31m-=-\33[m' * 20)
valor1 = float(input('Digite um valor:'))
valor2 = float(input('Digite outro valor:'))

print('\33[31m-=-\33[m' * 20)
if valor1 > valor2:
    print('\33[31m{}\33[m é maior que \33[34m{}\33[m'.format(valor1, valor2))
elif valor2 > valor1:
    print('\33[31m{}\33[m é maior que \33[34m{}\33[m'.format(valor2, valor1))
else:
    print('Os valores são iguais!')
print('\33[31m-=-\33[m' * 20)
