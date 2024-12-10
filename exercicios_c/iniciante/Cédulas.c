/*
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

Exemplo de Entrada	Exemplo de Saída
576

576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00

11257

11257
112 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
0 nota(s) de R$ 1,00

503

503
5 nota(s) de R$ 100,00
0 nota(s) de R$ 50,00
0 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
0 nota(s) de R$ 5,00
1 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
*/

#include <stdio.h>

int main(void) {
    int dinheiro, cem_reais, cinquenta_reais, vinte_reais, dez_reais, cinco_reais, dois_reais, um_real;

    scanf("%d", &dinheiro);

    cem_reais = dinheiro / 100;
    cinquenta_reais = (dinheiro % 100) / 50;
    vinte_reais = (dinheiro % 100 % 50) / 20;
    dez_reais = (dinheiro % 100 % 50 % 20) / 10;
    cinco_reais = (dinheiro % 100 % 50 % 20 % 10) / 5;
    dois_reais = (dinheiro % 100 % 50 % 20 % 10 % 5) / 2;
    um_real = (dinheiro % 100 % 50 % 20 % 10 % 5 % 2) / 1;

    printf("%d\n", dinheiro);
    printf("%d nota(s) de R$ 100,00\n", cem_reais);
    printf("%d nota(s) de R$ 50,00\n", cinquenta_reais);
    printf("%d nota(s) de R$ 20,00\n", vinte_reais);
    printf("%d nota(s) de R$ 10,00\n", dez_reais);
    printf("%d nota(s) de R$ 5,00\n", cinco_reais);
    printf("%d nota(s) de R$ 2,00\n", dois_reais);
    printf("%d nota(s) de R$ 1,00\n", um_real);
    return 0;
}
