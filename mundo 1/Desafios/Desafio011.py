largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a largura da parede: '))
area = largura * altura
tinta = area / 2
print('Você precisa de \33[1:41m{}\33[m litros de tinta...'.format(tinta))