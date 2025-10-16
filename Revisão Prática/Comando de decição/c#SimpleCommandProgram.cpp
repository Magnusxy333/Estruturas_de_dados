// Comandos de Decisão em C++
#include <iostream>

int main() {
    int num1;
    
    std::cout << "Digite um número inteiro (positivo, negativo ou zero): ";
    
    if (!(std::cin >> num1)) {
        std::cerr << "Erro: Entrada inválida." << std::endl;
        return 1;
    }
    
    std::cout << "\n--- Classificação (C++) ---" << std::endl;
    
    // Comandos de Decisão: if, else if, else
    if (num1 > 0) {
        std::cout << "O número " << num1 << " é POSITIVO." << std::endl;
    } else if (num1 < 0) {
        std::cout << "O número " << num1 << " é NEGATIVO." << std::endl;
    } else {
        std::cout << "O número " << num1 << " é ZERO." << std::endl;
    }
    
    return 0;
}