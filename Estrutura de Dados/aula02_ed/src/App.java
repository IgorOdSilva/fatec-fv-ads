import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        calcular();
    }

    public static void calcular() {
        float ent1;
        float ent2;
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o 1º Numero: ");
        ent1 = sc.nextFloat();
        System.out.print("Digite o 2º Numero: ");
        ent2 = sc.nextFloat();

        System.out.println("A Soma é:"+ (ent1+ent2));
        System.out.println("A Subtração é:"+ (ent1-ent2));
        System.out.println("A Multiplicação é:"+ (ent1*ent2));
        System.out.println("A Divisão é:"+ (ent1/ent2));

    }
}
