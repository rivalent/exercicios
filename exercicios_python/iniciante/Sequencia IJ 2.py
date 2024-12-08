'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo

Exemplo de Entrada	Exemplo de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
'''

i = 1
j = 7

while i <= 9:
    for repeticoes in range(3):
        print(f"I={i} J={j}")
        j -= 1
    i += 2
    j += 3
