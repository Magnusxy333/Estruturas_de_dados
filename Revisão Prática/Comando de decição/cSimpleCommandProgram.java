// Comandos de Decisão em Java
import java.util.Scanner;

public class ComandosDecisao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro (positivo, negativo ou zero): ");
        
        if (scanner.hasNextInt()) {
            int num1 = scanner.nextInt();
            
            System.out.println("\n--- Classificação (Java) ---");
            
            // Comandos de Decisão: if, else if, else
            if (num1 > 0) {
                System.out.println("O número " + num1 + " é POSITIVO.");
            } else if (num1 < 0) {
                System.out.println("O número " + num1 + " é NEGATIVO.");
            } else {
                System.out.println("O número " + num1 + " é ZERO.");
            }
        } else {
            System.out.println("Erro: Entrada inválida.");
        }
        scanner.close();
    }
}