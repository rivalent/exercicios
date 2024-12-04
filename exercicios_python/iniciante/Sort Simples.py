'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.

Exemplo de Entrada	Exemplo de Saída
7 21 -14

-14
7
21

7
21
-14

-14 21 7

-14
7
21

-14
21
7
'''

n1, n2, n3 = map(int, input().split())
numeros_antes = n1, n2, n3
ordenados = sorted(numeros_antes)

print(f"{ordenados[0]}\n{ordenados[1]}\n{ordenados[2]}\n")
print(f"{numeros_antes[0]}\n{numeros_antes[1]}\n{numeros_antes[2]}")
