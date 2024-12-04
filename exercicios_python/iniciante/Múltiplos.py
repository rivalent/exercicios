'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

Entrada
A entrada contém valores inteiros.

Saída
A saída deve conter uma das mensagens conforme descrito acima.

Exemplo de Entrada	Exemplo de Saída
6 24

Sao Multiplos

6 25

Nao sao Multiplos
'''

numero1, numero2 = map(int, input().split())

if numero1 % numero2 == 0 or numero2 % numero1 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
