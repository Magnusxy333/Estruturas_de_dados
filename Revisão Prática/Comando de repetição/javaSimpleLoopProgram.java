// Comandos de Repetição em Java
import java.util.Scanner;

public class ComandosRepeticao {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro (limite de repetição, ex: 5): ");
        
        if (scanner.hasNextInt()) {
            int num1 = scanner.nextInt();
            
            System.out.println("\n--- Loop 'for' (Contagem de 1 a N) ---");
            // Loop for
            for (int i = 1; i <= num1; i++) {
                System.out.print(i + " ");
            }
            System.out.println();
            
            System.out.println("\n--- Loop 'while' (Contagem Regressiva) ---");
            // Loop while
            int contador = num1;
            while (contador >= 1) {
                System.out.print(contador + " ");
                contador--; // Decremento
            }
            System.out.println();
        } else {
            System.out.println("Erro: Entrada inválida.");
        }
        scanner.close();
    }
}