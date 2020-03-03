reta1 = float(input('Digite o tamanho da primera reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))
if (reta3 + reta2) > reta1 and (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2:
    print('\33[4:34mÉ possivel fazer um triangulo com as retas!')
else:
    print('\33[4:31mNão é possivel fazer um triangulo com as retas!')