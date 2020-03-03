temperatura = float(input('Digite a temperatura em Celcius: °C '))
firehigh = (temperatura * (9/5)) + 32
print('A temperatura de \33[4:32m{}\33[m°C corresponde a \33[4:31m{}\33[m°F!'.format(temperatura, firehigh))