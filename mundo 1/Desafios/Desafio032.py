from datetime import date
ano = int(input('Digite um ano ou 0 caso queira ver o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano \33[4:34mbissexto\33[m!')
else:
    print('Ano não \33[4:34mbissexto\33[m!')
