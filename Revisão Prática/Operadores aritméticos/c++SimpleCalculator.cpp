// Programa de Operadores Aritméticos em C++.
#include <iostream>
#include <iomanip> // Para formatar a saída decimal

int main() {
    const int CONSTANTE = 5;
    int num1;
    
    std::cout << "Programa de Operadores Aritméticos em C++." << std::endl;
    std::cout << "Digite um número inteiro: ";
    
    if (!(std::cin >> num1)) {
        std::cerr << "Erro: Entrada inválida." << std::endl;
        return 1;
    }
    
    // Operadores Aritméticos
    int soma = num1 + CONSTANTE;
    int sub = num1 - CONSTANTE;
    int mult = num1 * CONSTANTE;
    double div = (double) num1 / CONSTANTE; // Conversão para double
    int mod = num1 % CONSTANTE; 
    
    // Saída
    std::cout << "\n--- Resultados (C++) ---" << std::endl;
    std::cout << "Número digitado: " << num1 << ", Constante: " << CONSTANTE << std::endl;
    std::cout << "Adição: " << num1 << " + " << CONSTANTE << " = " << soma << std::endl;
    std::cout << "Subtração: " << num1 << " - " << CONSTANTE << " = " << sub << std::endl;
    std::cout << "Multiplicação: " << num1 << " * " << CONSTANTE << " = " << mult << std::endl;
    // Formatando a saída para duas casas decimais
    std::cout << std::fixed << std::setprecision(2); 
    std::cout << "Divisão: " << num1 << " / " << CONSTANTE << " = " << div << std::endl;
    std::cout << "Resto da Divisão (Módulo): " << num1 << " % " << CONSTANTE << " = " << mod << std::endl;
    
    return 0;
}