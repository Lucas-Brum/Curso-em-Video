print('\33[4:31m calculadore de IMC...\33[m')
peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite seu altura atual: '))
imc = peso/altura**2
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obsidade morbida.')
