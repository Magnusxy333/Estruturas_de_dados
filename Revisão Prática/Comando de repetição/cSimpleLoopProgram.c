// Comandos de Repetição em C
#include <stdio.h>

int main() {
    int num1;
    
    printf("Digite um número inteiro (limite de repetição, ex: 5): ");
    
    if (scanf("%d", &num1) != 1) {
        printf("Erro: Entrada inválida.\n");
        return 1;
    }
    
    printf("\n--- Loop 'for' (Contagem de 1 a N) ---\n");
    // Loop for
    for (int i = 1; i <= num1; i++) {
        printf("%d ", i);
    }
    printf("\n");
    
    printf("\n--- Loop 'while' (Contagem Regressiva) ---\n");
    // Loop while
    int contador = num1;
    while (contador >= 1) {
        printf("%d ", contador);
        contador--; // Decremento
    }
    printf("\n");
    
    return 0;
}