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
    1: 0.15 * 100,
    2: 0.12 * 100,
    3: 0.10 * 100,
    4: 0.07 * 100,
    5: 0.04 * 100
}

salario = float(input())

if salario >= 0 and salario <= 400:
    aumento = salario * (reajuste[1] / 100)
    novo_salario = salario + aumento
    valor_acrescentado = aumento
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {valor_acrescentado:.2f}")
    print(f"Em percentual: {reajuste[1]:.0f} %")
elif salario >= 400.01 and salario <= 800:
    aumento = salario * (reajuste[2] / 100)
    novo_salario = salario + aumento
    valor_acrescentado = aumento
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {valor_acrescentado:.2f}")
    print(f"Em percentual: {reajuste[2]:.0f} %")
elif salario >= 800.01 and salario <= 1200:
    aumento = salario * (reajuste[3] / 100)
    novo_salario = salario + aumento
    valor_acrescentado = aumento
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {valor_acrescentado:.2f}")
    print(f"Em percentual: {reajuste[3]:.0f} %")
elif salario >= 1200.01 and salario <= 2000:
    aumento = salario * (reajuste[4] / 100)
    novo_salario = salario + aumento
    valor_acrescentado = aumento
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {valor_acrescentado:.2f}")
    print(f"Em percentual: {reajuste[4]:.0f} %")
elif salario >= 2000.01:
    aumento = salario * (reajuste[5] / 100)
    novo_salario = salario + aumento
    valor_acrescentado = aumento
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {valor_acrescentado:.2f}")
    print(f"Em percentual: {reajuste[5]:.0f} %")
