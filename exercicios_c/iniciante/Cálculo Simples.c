/*
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$". O valor deverá ser apresentado com 2 casas após o ponto.

Exemplos de Entrada	Exemplos de Saída
12 1 5.30
16 2 5.10

VALOR A PAGAR: R$ 15.50

13 2 15.30
161 4 5.20

VALOR A PAGAR: R$ 51.40

1 1 15.10
2 1 15.10

VALOR A PAGAR: R$ 30.20
*/

#include <stdio.h>

int main(void) {
    int cod_peca1, numeros_peca1, cod_peca2, numero_peca2;
    float valor_peca1, valor_peca2, preco_total;

    scanf("%d %d %f", &cod_peca1, &numeros_peca1, &valor_peca1);
    scanf("%d %d %f", &cod_peca2, &numero_peca2, &valor_peca2);

    preco_total = (numeros_peca1 * valor_peca1) + (numero_peca2 * valor_peca2);
    printf("VALOR A PAGAR: R$ %.2f\n", preco_total);
    return 0;
}
