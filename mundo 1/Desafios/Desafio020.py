from random import shuffle
aluno1 = str(input('Digite o nome de um aluno: '))
aluno2 = str(input('Digite o nome de outro aluno: '))
aluno3 = str(input('Digite o nome de outro aluno: '))
aluno4 = str(input('Digite o nome de outroaluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação de trabalho é : \33[1:36m{}\33[m'.format(lista))