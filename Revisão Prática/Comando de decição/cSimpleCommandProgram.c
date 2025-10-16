// Comandos de Decisão em C
#include <stdio.h>

int main() {
    int num1;
    
    printf("Digite um número inteiro (positivo, negativo ou zero): ");
    
    if (scanf("%d", &num1) != 1) {
        printf("Erro: Entrada inválida.\n");
        return 1;
    }
    
    printf("\n--- Classificação (C) ---\n");
    
    // Comandos de Decisão: if, else if, else
    if (num1 > 0) {
        printf("O número %d é POSITIVO.\n", num1);
    } else if (num1 < 0) {
        printf("O número %d é NEGATIVO.\n", num1);
    } else {
        printf("O número %d é ZERO.\n", num1);
    }
    
    return 0;
}