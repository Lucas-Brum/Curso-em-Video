distancia = float(input('Qual a distancia da sua viagem?'))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da tua viagem vai ser \33[34m{}'.format(preço))
print('\33[32mBoa viagem!')
