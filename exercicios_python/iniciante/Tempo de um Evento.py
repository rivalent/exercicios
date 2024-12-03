'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

Entrada
Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.

Saída
Na saída, deve ser apresentada a duração do evento, no seguinte formato:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

Exemplo de Entrada	Exemplo de Saída
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)
'''

linha_dia_inicio = input()
dia_inicio = int(linha_dia_inicio.split()[1])
hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(" : "))

linha_dia_fim = input()
dia_fim = int(linha_dia_fim.split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(" : "))

if segundo_fim >= segundo_inicio:
    segundos = segundo_fim - segundo_inicio
else:
    segundos = (segundo_fim + 60) - segundo_inicio
    minuto_fim -= 1

if minuto_fim >= minuto_inicio:
    minutos = minuto_fim - minuto_inicio
else:
    minutos = (minuto_fim + 60) - minuto_inicio
    hora_fim -= 1

if hora_fim >= hora_inicio:
    horas = hora_fim - hora_inicio
else:
    horas = (hora_fim + 24) - hora_inicio
    dia_fim -= 1

dias = dia_fim - dia_inicio

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
