'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:


Salário	Percentual de Reajuste
0 - 400.00
400.01 - 800.00
800.01 - 1200.00
1200.01 - 2000.00
Acima de 2000.00

15%
12%
10%
7%
4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

Entrada
A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

Saída
Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste (ambos devem ser apresentados com 2 casas decimais) e o percentual de reajuste ganho, conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
400.00

Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %

800.01

Novo salario: 880.01
Reajuste ganho: 80.00
Em percentual: 10 %

2000.00

Novo salario: 2140.00
Reajuste ganho: 140.00
Em percentual: 7 %
'''

reajuste = {
    1: 15,
    2: 12,
    3: 10,
    4: 7,
    5: 4
}

salario = float(input())

if salario <= 400:
    indice = 1
elif salario <= 800:
    indice = 2
elif salario <= 1200:
    indice = 3
elif salario <= 2000:
    indice = 4
else:
    indice = 5

percentual = reajuste[indice]
aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {aumento:.2f}")
print(f"Em percentual: {percentual} %")
