// Programa de Operadores Aritméticos em C#.
using System;

public class OperadoresAritmeticos
{
    public static void Main(string[] args)
    {
        const int CONSTANTE = 5;
        
        Console.WriteLine("Programa de Operadores Aritméticos em C#.");
        Console.Write("Digite um número inteiro: ");
        
        // Tenta ler e converter a string para inteiro de forma segura
        if (int.TryParse(Console.ReadLine(), out int num1))
        {
            // Operadores Aritméticos
            int soma = num1 + CONSTANTE;
            int sub = num1 - CONSTANTE;
            int mult = num1 * CONSTANTE;
            // Conversão implícita de int para double para divisão
            double div = (double)num1 / CONSTANTE; 
            int mod = num1 % CONSTANTE; 
            
            // Saída
            Console.WriteLine($"\n--- Resultados (C#) ---");
            Console.WriteLine($"Número digitado: {num1}, Constante: {CONSTANTE}");
            Console.WriteLine($"Adição: {num1} + {CONSTANTE} = {soma}");
            Console.WriteLine($"Subtração: {num1} - {CONSTANTE} = {sub}");
            Console.WriteLine($"Multiplicação: {num1} * {CONSTANTE} = {mult}");
            Console.WriteLine($"Divisão: {num1} / {CONSTANTE} = {div:F2}"); // :F2 para 2 casas decimais
            Console.WriteLine($"Resto da Divisão (Módulo): {num1} % {CONSTANTE} = {mod}");
        }
        else
        {
            Console.WriteLine("Erro: Entrada inválida.");
        }
    }
}