palavra = (input('Digite algo: '))
print('O tipo \33[4:34mprimitivo\33[m deste valor é :', type(palavra))
print('Só tem \33[4:34mespaços\33[m? ', palavra.isspace())
print('É um \33[4:34mnumero\33[m? ', palavra.isalnum())
print('É \33[4:34malfabetico\33[m? ',palavra.isalpha())
print('É \33[4:34malfanumerico\33[m', palavra.isalnum())
print('Esta em \33[4:34mmaiúsculas\33[m?', palavra.isupper())
print('Esta em \33[4:34mminuscula?\33[m ', palavra.islower())
print('Esta \33[4:34mcapitalizada\33[m? ', palavra.istitle())




