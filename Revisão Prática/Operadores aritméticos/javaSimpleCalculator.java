// Programa de Operadores Aritméticos em Java.
import java.util.Scanner;

public class OperadoresAritmeticos {
    public static void main(String[] args) {
        final int CONSTANTE = 5;
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Programa de Operadores Aritméticos em Java.");
        System.out.print("Digite um número inteiro: ");
        
        if (scanner.hasNextInt()) {
            int num1 = scanner.nextInt();
            
            // Operadores Aritméticos
            int soma = num1 + CONSTANTE;
            int sub = num1 - CONSTANTE;
            int mult = num1 * CONSTANTE;
            // Conversão para double para obter resultado decimal
            double div = (double) num1 / CONSTANTE; 
            int mod = num1 % CONSTANTE; 
            
            // Saída
            System.out.println("\n--- Resultados (Java) ---");
            System.out.println("Número digitado: " + num1 + ", Constante: " + CONSTANTE);
            System.out.println("Adição: " + num1 + " + " + CONSTANTE + " = " + soma);
            System.out.println("Subtração: " + num1 + " - " + CONSTANTE + " = " + sub);
            System.out.println("Multiplicação: " + num1 + " * " + CONSTANTE + " = " + mult);
            System.out.println("Divisão: " + num1 + " / " + CONSTANTE + " = " + div);
            System.out.println("Resto da Divisão (Módulo): " + num1 + " % " + CONSTANTE + " = " + mod);
        } else {
            System.out.println("Erro: Entrada inválida.");
        }
        
        scanner.close();
    }
}