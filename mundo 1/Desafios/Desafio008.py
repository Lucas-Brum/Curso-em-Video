print('Conversor de metros para \33[1:41mcentimetros\33[m e \33[1:42mmilimetros:\33[m')
tamanho = float(input('\33[1:43mMetros\33[m : '))
print('\33[1:33m{}\33[m metros são \33[1:31m{:.0f}\33[m centimetros ou \33[1:32m{:.0f}\33[m milimetros'.format(tamanho, tamanho * 100, tamanho * 1000))
