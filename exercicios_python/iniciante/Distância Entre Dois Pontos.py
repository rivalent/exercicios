'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia = sqrt de (x2 - x1)² + (y2 - y1)²

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

Exemplo de Entrada	Exemplo de Saída
1.0 7.0
5.0 9.0

4.4721

-2.5 0.4
12.1 7.3

16.1484

2.5 -0.4
-12.2 7.0

16.4575
'''
from math import sqrt

linha1 = input()
linha2 = input()

separa_linha1 = [float(n) for n in linha1.split()]
separa_linha2 = [float(n) for n in linha2.split()]

x1 = separa_linha1[0]
y1 = separa_linha1[1]
x2 = separa_linha2[0]
y2 = separa_linha2[1]

distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"{distancia:.4f}")
