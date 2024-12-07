'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

Exemplo de Entrada	Exemplo de Saída
6
-5

5

15
12

13

12
12

0
'''

x = int(input())
y = int(input())

inicio = min(x, y) + 1
fim = max(x, y)
soma_impares = 0

for numero in range(inicio, fim):
    if numero % 2 != 0:
        soma_impares += numero

print(soma_impares)
