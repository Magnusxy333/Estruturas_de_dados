import java.util.Scanner;

public class WhileLoopWithInput {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = 0;
        boolean startCountdown = false; 


        while (true) { 

            if (!startCountdown) { 
                System.out.print("Por favor ponha um número positivo: ");

                if (scanner.hasNextInt()) {
                    number = scanner.nextInt();

                    if (number > 0) {

                        startCountdown = true; 
                        
                    } else {
                        System.out.println("comando inválido, o número de deve ser positivo");
                    }
                } else {
                    System.out.println("comando inválido, o numéro deve ser inteiro");

                    scanner.next(); 
                }
            } 

            else { 
                if (number > 0) {
                    System.out.println("\nIniciando a contagem regressiva:");
                    int i = number;
                    
                    while (i >= 1) { 
                        System.out.println(i);
                        i--;
                    }
                    System.out.println("Fogo! 🚀");
                }
                
                break; 
            }
        }

        scanner.close();
    }
}