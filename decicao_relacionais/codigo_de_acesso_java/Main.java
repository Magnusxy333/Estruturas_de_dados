import java.util.*;

public class Main {
  
  
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
      
      System.out.println("Digite a senha:");
      String r = input.nextLine();
      
      
      if (r.equals("Admin123")) {
       System.out.println("Bem-vindo, Administrador!");
      }
      
      else if (r.equals("User123")) {
        System.out.println("Bem-vindo, Usuário!");
      }
      
      else {
        System.out.println("Senha incorreta!");
      }
  }
}