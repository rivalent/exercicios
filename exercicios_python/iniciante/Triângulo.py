'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.

Exemplo de Entrada	Exemplo de Saída
6.0 4.0 2.0

Area = 10.0

6.0 4.0 2.1

Perimetro = 12.1
'''

valores = input()
valores_separados = [float(v) for v in valores.split()]
r1 = valores_separados[0]
r2 = valores_separados[1]
r3 = valores_separados[2]

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    calculo_perimetro = r1 + r2 + r3
    print(f"Perimetro = {calculo_perimetro:.1f}")
else:
    calculo_area = ((r1 + r2) * r3) / 2
    print(f"Area = {calculo_area:.1f}")