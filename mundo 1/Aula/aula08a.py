import math, random, emoji
num = random.randint(1, 10)
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print(emoji.emojize('Ola, mundo :earth_americas:', use_aliases= True))
