print('\33[31m-=-\33[m' * 20)
print('Gerenciador de emprestimos imobiliarios...')
print('\33[31m-=-\33[m' * 20)
casa = float(input('Digite o valor total do imovel: R$'))
salario = float(input('Qual seu salario atual: R$'))
ano = int(input('Em quantos anos deseja pagar: '))
mensalidade = casa / (ano*12)
print('\33[31m-=-\33[m' * 20)
if mensalidade <= (salario * 0.30):
    print('Sua prestação sera de \33[4:34m{:.2f}\33[m'.format(mensalidade))
else:
    print('\33[4:31mO imprestimo sera negado por exeder 30% do seu salario!')
print('\33[m\33[31m-=-\33[m' * 20)