// Comandos de Repetição em C#
using System;

public class ComandosRepeticao
{
    public static void Main(string[] args)
    {
        Console.Write("Digite um número inteiro (limite de repetição, ex: 5): ");
        
        if (int.TryParse(Console.ReadLine(), out int num1))
        {
            Console.WriteLine($"\n--- Loop 'for' (Contagem de 1 a N) ---");
            // Loop for
            for (int i = 1; i <= num1; i++)
            {
                Console.Write(i + " ");
            }
            Console.WriteLine();
            
            Console.WriteLine($"\n--- Loop 'while' (Contagem Regressiva) ---");
            // Loop while
            int contador = num1;
            while (contador >= 1)
            {
                Console.Write(contador + " ");
                contador--; // Decremento
            }
            Console.WriteLine();
        }
        else
        {
            Console.WriteLine("Erro: Entrada inválida.");
        }
    }
}