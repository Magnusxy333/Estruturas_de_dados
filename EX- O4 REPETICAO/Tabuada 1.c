#include <stdio.h>

int main() {
    int numero; 
    int i;      

    printf("Digite o número para ver a tabuada: ");
    scanf("%d", &numero);

    printf("\n--- Tabuada do %d ---\n", numero);

    for (i = 1; i <= 10; i++) {
        
        printf("%d x %d = %d\n", numero, i, numero * i);
        
    }

    return 0;
}