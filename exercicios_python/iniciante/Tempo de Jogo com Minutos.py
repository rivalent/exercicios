'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

Exemplo de Entrada	Exemplo de Saída
7 8 9 10

O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

7 7 7 7

O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)

7 10 8 9

O JOGO DUROU 0 HORA(S) E 59 MINUTO(S)
'''

hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

# Converter horas e minutos para minutos totais desde o início do dia
inicio_total = hora_inicio * 60 + minuto_inicio
fim_total = hora_fim * 60 + minuto_fim

# Calcular a diferença total de minutos
if fim_total <= inicio_total:
    duracao_total = (24 * 60 - inicio_total) + fim_total  # Caso o jogo passe da meia-noite
else:
    duracao_total = fim_total - inicio_total

# Converter a duração total de minutos em horas e minutos
duracao_horas = duracao_total // 60
duracao_minutos = duracao_total % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
