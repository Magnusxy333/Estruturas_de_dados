// Programa de Operadores Relacionais em Java.
import java.util.Scanner;

public class OperadoresRelacionais {
    public static void main(String[] args) {
        final int CONSTANTE = 10;
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Programa de Operadores Relacionais em Java.");
        System.out.print("Digite um número inteiro: ");
        
        if (scanner.hasNextInt()) {
            int num1 = scanner.nextInt();
            
            // Operadores Relacionais
            boolean igual = num1 == CONSTANTE;
            boolean diferente = num1 != CONSTANTE;
            boolean maior = num1 > CONSTANTE;
            boolean menor = num1 < CONSTANTE;
            boolean maiorIgual = num1 >= CONSTANTE;
            boolean menorIgual = num1 <= CONSTANTE;
            
            // Saída
            System.out.println("\n--- Comparando " + num1 + " e " + CONSTANTE + " (Java) ---");
            System.out.println("É igual a 10? (" + num1 + " == " + CONSTANTE + "): " + igual);
            System.out.println("É diferente de 10? (" + num1 + " != " + CONSTANTE + "): " + diferente);
            System.out.println("É maior que 10? (" + num1 + " > " + CONSTANTE + "): " + maior);
            System.out.println("É menor que 10? (" + num1 + " < " + CONSTANTE + "): " + menor);
            System.out.println("É maior ou igual a 10? (" + num1 + " >= " + CONSTANTE + "): " + maiorIgual);
            System.out.println("É menor ou igual a 10? (" + num1 + " <= " + CONSTANTE + "): " + menorIgual);
            
        } else {
            System.out.println("Erro: Entrada inválida.");
        }
        
        scanner.close();
    }
}