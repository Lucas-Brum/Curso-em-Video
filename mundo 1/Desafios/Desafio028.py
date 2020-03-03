from random import randint
from time import sleep
pc = randint(1, 10)
print('Pensando em um numero...')
sleep(3)
print('JÁ SEI!!!')
print('Digite e tente adivinhar o numero inteiro de 1 a 10 que pensei...')
numero = int(input('Qual sua aposta: '))
if pc == numero:
    print('\33[34mAcertou miseravel!')
else:
    print('\33[1:31mErrou o pc pensou no numero \33[4:34m{}\33[m\33[1:31m!'.format(pc))
