print('\33[4m-=-\33[m' * 20)
print('Qual sua categoria:')
idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Nadador mirim.')
elif idade <= 14:
    print('Nadador infatil.')
elif idade <=19:
    print('Nadador junior.')
elif idade == 20:
    print('Nadador sênior.')
else:
    print('Nadador master.')