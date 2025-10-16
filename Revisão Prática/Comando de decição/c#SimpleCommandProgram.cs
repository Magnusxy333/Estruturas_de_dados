// Comandos de Decisão em C#
using System;

public class ComandosDecisao
{
    public static void Main(string[] args)
    {
        Console.Write("Digite um número inteiro (positivo, negativo ou zero): ");
        
        if (int.TryParse(Console.ReadLine(), out int num1))
        {
            Console.WriteLine($"\n--- Classificação (C#) ---");
            
            // Comandos de Decisão: if, else if, else
            if (num1 > 0)
            {
                Console.WriteLine($"O número {num1} é POSITIVO.");
            }
            else if (num1 < 0)
            {
                Console.WriteLine($"O número {num1} é NEGATIVO.");
            }
            else
            {
                Console.WriteLine($"O número {num1} é ZERO.");
            }
        }
        else
        {
            Console.WriteLine("Erro: Entrada inválida.");
        }
    }
}