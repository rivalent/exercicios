'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
5 2
6 3
5 0

2 3 4 5 Sum=14
3 4 5 6 Sum=18
'''


while True:
    m, n = map(int, input().split())

    inicio = min(m, n)
    fim = max(m, n)

    if n <= 0 or m <= 0:
        break
    
    soma = sum(range(inicio, fim + 1))

    print(f"{' '.join(map(str, range(inicio, fim + 1)))} Sum={soma}")
