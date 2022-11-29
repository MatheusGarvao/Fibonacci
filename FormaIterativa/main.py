import time
import csv

quantidade = 0
num1 = 0
num2 = 1
with open('valoresobtidos.csv', 'w', newline='') as file:
    escrever = csv.DictWriter(file, fieldnames=['numteste', 'quantidade', 'tempo'])
    escrever.writeheader()
    for i in range(1, 3001):
        tempoInicial = time.time()
        for x in range(i-2):
            quantidade += 1
            resultado = num1+num2
            num1, num2 = num2, resultado
        tempoFinal = time.time()
        escrever.writerow({'numteste': i, 'quantidade': quantidade, 'tempo': (tempoFinal-tempoInicial)})
        quantidade = 0
