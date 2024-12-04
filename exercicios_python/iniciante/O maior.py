'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

maiorAB = a + b + abs(a - b) / 2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada	Exemplos de Saída
7 14 106

106 eh o maior

217 14 6

217 eh o maior
'''

valor1, valor2, valor3 = map(int, input().split())

maior = (valor1 + valor2 + abs(valor1 - valor2)) / 2
maior_abs = (maior + valor3 + abs(valor3 - maior)) / 2

print(f"{maior_abs:.0f} eh o maior")
