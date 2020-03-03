print('Somador de valores...')
print('\33[1:36m-=-\33[m' * 20)
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('\33[1:34m-=-\33[m' * 20)
print('A soma entre \33[34m{}\33[m e \33[34m{}\33[m é  igual a \33[1:31m{}\33[m!'.format(n1, n2, s))
print('\33[1:33m-=-\33[m' * 20)