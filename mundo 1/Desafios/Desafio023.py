import random
numero =int( random.randint(0, 9999))
unidade = numero // 1 % 10
dezena= numero // 10 % 10
centena= numero // 100 % 10
milhar= numero // 1000 % 10
print('Numero escolhido por a maquina :{}'.format(numero))
print('Unidade: \33[3:37m{} \33[m'.format(unidade))
print('Dezena: \33[7:31m{}\33[m'.format(dezena))
print('Centena: \33[4:34m{}\33[m'.format(centena))
print('Milhar: \33[1:35m:35{}\33[m'.format(milhar))