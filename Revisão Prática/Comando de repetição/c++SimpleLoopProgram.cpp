// Comandos de Repetição em C++
#include <iostream>

int main() {
    int num1;
    
    std::cout << "Digite um número inteiro (limite de repetição, ex: 5): ";
    
    if (!(std::cin >> num1)) {
        std::cerr << "Erro: Entrada inválida." << std::endl;
        return 1;
    }
    
    std::cout << "\n--- Loop 'for' (Contagem de 1 a N) ---" << std::endl;
    // Loop for
    for (int i = 1; i <= num1; i++) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    
    std::cout << "\n--- Loop 'while' (Contagem Regressiva) ---" << std::endl;
    // Loop while
    int contador = num1;
    while (contador >= 1) {
        std::cout << contador << " ";
        contador--; // Decremento
    }
    std::cout << std::endl;
    
    return 0;
}