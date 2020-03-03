preco = float(input('Digite o valor do produto: '))
desconto = preco - (preco * 0.05)
print('O valor do item com \33[4:31mdesconto\33[m fica {:.2F}.'.format(desconto))