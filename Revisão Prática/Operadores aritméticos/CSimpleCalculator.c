// Programa de Operadores Aritméticos em C.
#include <stdio.h>

int main() {
    const int CONSTANTE = 5;
    int num1;
    
    printf("Programa de Operadores Aritméticos em C.\n");
    printf("Digite um número inteiro: ");
    
    if (scanf("%d", &num1) != 1) {
        printf("Erro: Entrada inválida.\n");
        return 1;
    }
    
    // Operadores Aritméticos
    int soma = num1 + CONSTANTE;
    int sub = num1 - CONSTANTE;
    int mult = num1 * CONSTANTE;
    double div = (double) num1 / CONSTANTE; // Conversão para double
    int mod = num1 % CONSTANTE; 
    
    // Saída
    printf("\n--- Resultados (C) ---\n");
    printf("Número digitado: %d, Constante: %d\n", num1, CONSTANTE);
    printf("Adição: %d + %d = %d\n", num1, CONSTANTE, soma);
    printf("Subtração: %d - %d = %d\n", num1, CONSTANTE, sub);
    printf("Multiplicação: %d * %d = %d\n", num1, CONSTANTE, mult);
    printf("Divisão: %d / %d = %.2f\n", num1, CONSTANTE, div); // %.2f para 2 casas decimais
    printf("Resto da Divisão (Módulo): %d %% %d = %d\n", num1, CONSTANTE, mod);
    
    return 0;
}