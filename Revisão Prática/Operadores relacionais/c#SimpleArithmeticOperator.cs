// Programa de Operadores Relacionais em C#.
using System;

public class OperadoresRelacionais
{
    public static void Main(string[] args)
    {
        const int CONSTANTE = 10;
        
        Console.WriteLine("Programa de Operadores Relacionais em C#.");
        Console.Write("Digite um número inteiro: ");
        
        // Tenta ler e converter a string para inteiro
        if (int.TryParse(Console.ReadLine(), out int num1))
        {
            // Operadores Relacionais
            bool igual = num1 == CONSTANTE;
            bool diferente = num1 != CONSTANTE;
            bool maior = num1 > CONSTANTE;
            bool menor = num1 < CONSTANTE;
            bool maiorIgual = num1 >= CONSTANTE;
            bool menorIgual = num1 <= CONSTANTE;
            
            // Saída
            Console.WriteLine($"\n--- Comparando {num1} e {CONSTANTE} (C#) ---");
            Console.WriteLine($"É igual a 10? ({num1} == {CONSTANTE}): {igual}");
            Console.WriteLine($"É diferente de 10? ({num1} != {CONSTANTE}): {diferente}");
            Console.WriteLine($"É maior que 10? ({num1} > {CONSTANTE}): {maior}");
            Console.WriteLine($"É menor que 10? ({num1} < {CONSTANTE}): {menor}");
            Console.WriteLine($"É maior ou igual a 10? ({num1} >= {CONSTANTE}): {maiorIgual}");
            Console.WriteLine($"É menor ou igual a 10? ({num1} <= {CONSTANTE}): {menorIgual}");
        }
        else
        {
            Console.WriteLine("Erro: Entrada inválida.");
        }
    }
}