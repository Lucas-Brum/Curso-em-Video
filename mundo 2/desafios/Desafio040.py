print('Sistema de notas!')
print('\33[34m-=-\33[m' * 20)
portugues = int(input('Digite nota em portugues: '))
math = int(input('Digite nota em portugues: '))
prog = int(input('Digite nota em portugues: '))
media = ((portugues + math + prog)/3)
print('\33[34m-=-\33[m' * 20)
if media < 5:
    print('{} é uma nota muito abaixo da media!'.format(media))
elif media >= 5 and media < 7:
    print('{} esta abaixo da medio mas ainda pode recuperar'.format(media))
else:
    print('Aprovado!')
print('\33[34m-=-\33[m' * 20)