nome = str(input('Qual seu nome?'))
if nome == 'Lucas':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Paulo' or nome == 'Pedro':
    print('Seu nome é bem popular...')
elif nome in 'Fran Franciele Leila Lais':
    print('Um nome feminino bonito!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))