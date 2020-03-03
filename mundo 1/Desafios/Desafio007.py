nome = str(input('Digite o nome do aluno: '))
matematica = float(input("Digite a nota do aluno em \33[1:41mMatematica: \33[m "))
portugues = float(input("Digite a nota do aluno em \33[1:42mportugues: \33[m "))
filosofia = float(input("Digite a nota do aluno em \33[1:43mfilosofia: \33[m "))
programacao = float(input("Digite a nota do aluno em \33[1:44mprogramação: \33[m "))

print('Calculando a media...')

print('A media final do \33[1:41m{}\33[m ficou : \33[1:41m{}\33[m.'.format(nome, (matematica + portugues + filosofia + programacao)/4 ))