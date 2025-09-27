using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace AvaliacaoNota
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Console.WriteLine("Por favor, digite sua nota (somente o número inteiro):");

            string input = Console.ReadLine();
            
            int nota;

            if (int.TryParse(input, out nota))
            {
                // **LÓGICA CORRIGIDA**

                if (nota <= 5)
                { 
                    Console.WriteLine("Você foi reprovado."); 
                } 
                else if (nota <= 6) 
                { 
                    Console.WriteLine("Você está de recuperação.");
                } 
                else 
                { 
                    Console.WriteLine("Parabéns! Você foi aprovado."); 
                }
            }
            else
            {
                Console.WriteLine("Erro: Você precisa digitar um número válido.");
            }
        }
    }
}