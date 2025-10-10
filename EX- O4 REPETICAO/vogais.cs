using System;
using System.Collections.Generic;
using System.Linq;

public class ContadorDeVogais
{
    public static void Main(string[] args)
    {
        // Define as vogais, tanto minúsculas quanto maiúsculas.
        // O C# tem uma maneira mais simples de fazer isso.
        char[] vogais = { 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' };

        // Pede a entrada ao usuário (em C# o 'input' é feito com Console.ReadLine())
        Console.Write("Digite uma palavra: ");
        string entradaCrua = Console.ReadLine();

        // Lista para armazenar as vogais localizadas, semelhante a 'vogais_localizadas = []' em Python.
        List<char> vogaisLocalizadas = new List<char>();

        // Verifica se a entrada não é nula para evitar erros.
        if (!string.IsNullOrEmpty(entradaCrua))
        {
            // O laço 'foreach' em C# é muito eficiente para iterar sobre os caracteres de uma string.
            foreach (char caractere in entradaCrua)
            {
                // Em C#, podemos usar o método 'Contains' da lista 'vogais' para verificar
                // se o caractere atual é uma vogal.
                if (vogais.Contains(caractere))
                {
                    vogaisLocalizadas.Add(caractere);
                }
            }
        }

        // A quantidade de vogais é o número de elementos na lista 'vogaisLocalizadas'.
        int qtVogais = vogaisLocalizadas.Count;

        // Imprime o resultado. O C# também suporta interpolação de strings ($"...")
        // e para formatar a lista, usamos 'string.Join' para exibir de forma legível.
        Console.WriteLine($"A palavra {entradaCrua} tem {qtVogais} vogais.");
        Console.WriteLine($"As vogais localizadas em {entradaCrua} foram: {string.Join(", ", vogaisLocalizadas)}");
    }
}