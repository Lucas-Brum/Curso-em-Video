numero1 = float(input('Primeiro numero: '))
numero2 = float(input('Segundo Numero: '))
numero3 = float(input('Terceiro numero: '))
menor = numero1
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    menor = numero2
if numero3 > numero1 and numero3 > numero2:
    menor = numero3
if numero2 < numero1 and numero2 < numero3:
    maior = numero2
if numero3 < numero1 and numero3 < numero2:
    maior = numero3

print('O maior valor é \33[36m{}\33[m'.format(maior))
print('O menor valor é \33[35m{}\33[m'.format(menor))