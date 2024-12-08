'''
Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

Entrada
Não há nenhuma entrada neste problema.

Saída
Imprima a sequencia conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
'''
i = 0.0

while i <= 2:
    j = i + 1
    for repeticoes in range(3):
        if i == int(i):
            if j == int(j):
                print(f"I={int(i)} J={int(j)}")
            else:
                print(f"I={int(i)} J={j:.1f}")
        else:
            print(f"I={i:.1f} J={j:.1f}")
        j += 1
    i = round(i + 0.2, 1)
