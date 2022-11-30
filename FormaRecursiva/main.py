import time

q = 0


def fibonacci(n):
    global q
    q += 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def menu():
    global q
    arquivoCSV = open('fibanacci.csv', 'a')
    arquivoCSV.write('valorN, tempoDemorado, quatidadePercorrida\n')
    n = int(input("Informe o numero desejado: "))

    for val in range(1, n + 1):
        tempoInicial = time.time()
        valorN = fibonacci(val)
        tempoFinal = time.time()
        print(val)
        arquivoCSV.write(str(val) + ',' + str(tempoFinal - tempoInicial) + ',' + str(q) + '\n')
        q = 0
    arquivoCSV.close()


if __name__ == '__main__':
    menu()
