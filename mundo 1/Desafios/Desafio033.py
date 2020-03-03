
numero1 = float(input('Primeiro numero: '))
numero2 = float(input('Segundo Numero: '))
numero3 = float(input('Terceiro numero: '))

if numero1 > numero2 and numero1 > numero3:
        print('O numero \33[31m{}\33[m é o \33[31mmaior\33[m!'.format(numero1))
if numero2 > numero1 and numero2 > numero3:
        print('O numero \33[31m{}\33[m é o \33[31mmaior\33[m!'.format(numero2))
if numero3 > numero1 and numero3 > numero2:
        print('O numero \33[31m{}\33[m é o \33[31mmaior\33[m!'.format(numero3))
if numero1 < numero2 and numero1 < numero3:
        print('O numero \33[34m{}\33[m é o \33[34mmenor\33[m!'.format(numero1))
if numero2 < numero1 and numero2 < numero3:
        print('O numero \33[34m{}\33[m é o \33[34mmenor\33[m!'.format(numero2))
if numero3 < numero1 and numero3 < numero2:
        print('O numero \33[34m{}\33[m é o \33[34mmenor\33[m!'.format(numero3))