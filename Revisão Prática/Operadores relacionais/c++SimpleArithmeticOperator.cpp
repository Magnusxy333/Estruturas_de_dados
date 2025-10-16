// Programa de Operadores Relacionais em C++.
#include <iostream>

int main() {
    const int CONSTANTE = 10;
    int num1;
    
    std::cout << "Programa de Operadores Relacionais em C++." << std::endl;
    std::cout << "Digite um número inteiro: ";
    
    if (!(std::cin >> num1)) {
        std::cerr << "Erro: Entrada inválida." << std::endl;
        return 1;
    }
    
    // Operadores Relacionais
    bool igual = num1 == CONSTANTE;
    bool diferente = num1 != CONSTANTE;
    bool maior = num1 > CONSTANTE;
    bool menor = num1 < CONSTANTE;
    bool maior_igual = num1 >= CONSTANTE;
    bool menor_igual = num1 <= CONSTANTE;
    
    // Saída. Usando 'std::boolalpha' para imprimir TRUE/FALSE em vez de 1/0
    std::cout << "\n--- Comparando " << num1 << " e " << CONSTANTE << " (C++) ---" << std::endl;
    std::cout << std::boolalpha; // Configura o cout para imprimir true/false
    
    std::cout << "É igual a 10? (" << num1 << " == " << CONSTANTE << "): " << igual << std::endl;
    std::cout << "É diferente de 10? (" << num1 << " != " << CONSTANTE << "): " << diferente << std::endl;
    std::cout << "É maior que 10? (" << num1 << " > " << CONSTANTE << "): " << maior << std::endl;
    std::cout << "É menor que 10? (" << num1 << " < " << CONSTANTE << "): " << menor << std::endl;
    std::cout << "É maior ou igual a 10? (" << num1 << " >= " << CONSTANTE << "): " << maior_igual << std::endl;
    std::cout << "É menor ou igual a 10? (" << num1 << " <= " << CONSTANTE << "): " << menor_igual << std::endl;
    
    return 0;
}