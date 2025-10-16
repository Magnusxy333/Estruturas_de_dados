// Programa de Operadores Relacionais em C.
#include <stdio.h>
#include <stdbool.h> // Necessário para usar o tipo 'bool' em C99 ou superior

int main() {
    const int CONSTANTE = 10;
    int num1;
    
    printf("Programa de Operadores Relacionais em C.\n");
    printf("Digite um número inteiro: ");
    
    if (scanf("%d", &num1) != 1) {
        printf("Erro: Entrada inválida.\n");
        return 1;
    }
    
    // Operadores Relacionais (o resultado será 1 para True, 0 para False)
    bool igual = num1 == CONSTANTE;
    bool diferente = num1 != CONSTANTE;
    bool maior = num1 > CONSTANTE;
    bool menor = num1 < CONSTANTE;
    bool maior_igual = num1 >= CONSTANTE;
    bool menor_igual = num1 <= CONSTANTE;
    
    // Saída. Usamos %d para imprimir o valor booleano (1 ou 0)
    printf("\n--- Comparando %d e %d (C) ---\n", num1, CONSTANTE);
    printf("É igual a 10? (%d == %d): %d\n", num1, CONSTANTE, igual);
    printf("É diferente de 10? (%d != %d): %d\n", num1, CONSTANTE, diferente);
    printf("É maior que 10? (%d > %d): %d\n", num1, CONSTANTE, maior);
    printf("É menor que 10? (%d < %d): %d\n", num1, CONSTANTE, menor);
    printf("É maior ou igual a 10? (%d >= %d): %d\n", num1, CONSTANTE, maior_igual);
    printf("É menor ou igual a 10? (%d <= %d): %d\n", num1, CONSTANTE, menor_igual);
    
    return 0;
}