portugues = float(input('Digite a primeira nota: '))
matematica = float(input('Digite a segunda nota: '))
media = (portugues + matematica)/2
print('Sua media foi {:.1f}'.format(media))
print('Aluno aprovado' if media >= 6 else 'Aluno reprovado! :/')