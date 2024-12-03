'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

Exemplo de Entrada	Exemplo de Saída
-5
0
-3
-4
12

3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)
'''

pares = 0
impares = 0
positivos = 0
negativos = 0

for n in range(5):
    numeros = int(input())

    if numeros % 2 == 0:
        pares += 1
    if numeros % 2 != 0:
        impares += 1
    if numeros > 0:
        positivos += 1
    if numeros < 0:
        negativos += 1

print(f"{pares} valor(es) par(es)\n{impares} valor(es) impar(es)\n{positivos} valor(es) positivo(s)\n{negativos} valor(es) negativo(s)")
