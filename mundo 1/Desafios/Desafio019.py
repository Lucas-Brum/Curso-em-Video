import random
aluno1 = str(input('Digite o nome do aluno: '))
aluno2 = str(input('Digite o nome de outro aluno: '))
aluno3 = str(input('Digite o nome de outro aluno: '))
aluno4 = str(input('Digite o nome de outro aluno: '))
lista = [aluno1, aluno2, aluno3, aluno3]
escolhido = random.choice(lista)
print('O aluno escolhido foi \33[1:30:47m{}\33[m'.format(escolhido))