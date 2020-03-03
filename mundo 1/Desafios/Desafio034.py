salario = float(input('Digite seu salario para ver seu aumento: '))
if salario < 1250:
    print('Seu salario agora vai ser: \33[31m{}'.format((salario * 0.15)+salario))
else:
    print('Seu salario agora vai ser: \33[34m{}'.format((salario * 0.10)+salario))
