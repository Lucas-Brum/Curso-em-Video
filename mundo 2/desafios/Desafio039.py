print('Exercito brasileiro!')
print('\33[34m-=-\33[m' * 20)
idade = int(input('Digite sua idade: '))
print('\33[34m-=-\33[m' * 20)
if idade < 18:
    print('Faltam {} anos para se alistar!'.format(18-idade))
elif idade > 18:
    print('Já se passaram {} anos do seu alistamento'.format(idade - 18))
else:
    print('Você já pode se alistar!')
print('\33[34m-=-\33[m' * 20)