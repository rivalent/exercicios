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

numeros = input()
numeros_mesmalinha = [int(n) for n in numeros.split()]
numeros_antes = numeros_mesmalinha[:]
numeros_mesmalinha.sort()
n1, n2, n3 = numeros_mesmalinha

print(f"{n1}\n{n2}\n{n3}\n")
print(f"{numeros_antes[0]}\n{numeros_antes[1]}\n{numeros_antes[2]}")