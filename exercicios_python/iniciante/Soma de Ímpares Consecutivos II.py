'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.

Exemplo de Entrada	Exemplo de Saída
7

4 5

13 10

6 4

3 3

3 5

3 4

3 8

0

11

5

0

0

0

12
'''

teste = int(input())

for repeticoes in range(teste):
    x, y = map(int, input().split())

    inicio = min(x, y) + 1
    fim = max(x, y)
    soma_impares = 0

    for numero in range(inicio, fim):
        if numero % 2 != 0:
            soma_impares += numero

    print(soma_impares)
