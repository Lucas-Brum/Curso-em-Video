frase = 'Curso em Video Python'
frase2 = '   Aprenda python  '
print(frase) #mostra a frase
print(frase[9]) #mostra apenas a posição 9 da frase
print(frase[9:13]) #mostra da posição 9 até a 13
print(frase[9:21:2]) #mostra da 9 até a posição 21 pulando de 2 em 2
print(frase[:5]) #mostra todos até o 5
print(frase[15:])#mostra da psição 15 em diante
print(frase[9::3])#mostra do 9 até o fim pulando de 3 em 3
print(len(frase))# mostra quantas letras tem a string
print(frase.count('o'))#conta quantos 'o' tem na frase
print(frase.count('o', 0, 13))#Mostra quantos 'o' tem do 0 ao 13
print(frase.find('deo'))#mostra aonde esta deo na string
print(frase.find('Android')) #mostra aonde esta a palavra android
print('curso' in frase) # Retorna true se encontrar a palavra e face se não encontrar
# add o python diferencia minusculas de maiusculas
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.replace('Python', 'Android'))#troca as palavras se encontrar a primeira
print(frase2.strip())#remove espaco do inicio e do fim
print(frase2.rstrip())#remove espaços a direita da frase
print(frase2.lstrip())#remove espaços a esquerda da frase
print(frase.split())# divide a frase em palavras numa lista
print('-'. join(frase2))# coloca traço entre os espaçoes de memoria
"""Se posso usar join + split para fazer coisas assim"""
print('-'.join(frase.split()))