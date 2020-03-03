salario = float(input('Digite o salario atual: '))
aumento = salario + (salario * 0.15)
print('O seu novo salario fica \33[4:31m{:.2F}\33[m.'.format(aumento))