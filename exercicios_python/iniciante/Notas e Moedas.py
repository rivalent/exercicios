'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada	Exemplo de Saída
576.73

NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01

4.00

NOTAS:
0 nota(s) de R$ 100.00
0 nota(s) de R$ 50.00
0 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
2 nota(s) de R$ 2.00
MOEDAS:
0 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
0 moeda(s) de R$ 0.01

91.01

NOTAS:
0 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
2 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
0 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
0 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
0 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
1 moeda(s) de R$ 0.01
'''

dinheiro = float(input())
dinheiro = round(dinheiro * 100)

cem_reais = dinheiro // 10000
cinquenta_reais = (dinheiro % 10000) // 5000
vinte_reais = (dinheiro % 10000 % 5000) // 2000
dez_reais = (dinheiro % 10000 % 5000 % 2000) // 1000
cinco_reais = (dinheiro % 10000 % 5000 % 2000 % 1000) // 500
dois_reais = (dinheiro % 10000 % 5000 % 2000 % 1000 % 500) // 200
um_real = (dinheiro % 10000 % 5000 % 2000 % 1000 % 500 % 200) // 100
cinquenta_centavos = (dinheiro % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100) // 50
vinteecinco_centavos = (dinheiro % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50) // 25
dez_centavos = (dinheiro % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25) // 10
cinco_centavos = (dinheiro % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 % 10) // 5
um_centavo = (dinheiro % 10000 % 5000 % 2000 % 1000 % 500 % 200 % 100 % 50 % 25 % 10 % 5) // 1

print("NOTAS:")
print(f"{cem_reais:.0f} nota(s) de R$ 100.00")
print(f"{cinquenta_reais:.0f} nota(s) de R$ 50.00")
print(f"{vinte_reais:.0f} nota(s) de R$ 20.00")
print(f"{dez_reais:.0f} nota(s) de R$ 10.00")
print(f"{cinco_reais:.0f} nota(s) de R$ 5.00")
print(f"{dois_reais:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{um_real:.0f} moeda(s) de R$ 1.00")
print(f"{cinquenta_centavos:.0f} moeda(s) de R$ 0.50")
print(f"{vinteecinco_centavos:.0f} moeda(s) de R$ 0.25")
print(f"{dez_centavos:.0f} moeda(s) de R$ 0.10")
print(f"{cinco_centavos:.0f} moeda(s) de R$ 0.05")
print(f"{um_centavo:.0f} moeda(s) de R$ 0.01")
