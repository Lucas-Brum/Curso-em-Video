quilometragem = float(input('Quantos quilometros você rodou com o carro?? \n'))
diarias = float(input('Quantos dias você esta com o carro? \n'))
total = (quilometragem * 0.15)+(diarias * 60)
print('O total a se pagar por o aluguel do carro é : \33[1:31m{} R$\33[m'.format(total))
