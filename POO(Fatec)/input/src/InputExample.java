import java.util.Scanner;

public class InputExample {
    private Scanner scanner;

    public InputExample() {
        this.scanner = new Scanner(System.in);
    }

    public void getImc() {
        System.out.print("Digite algo: ");
        String altura = scanner.nextLine();
        System.out.print("Digite algo: ");
        String peso = scanner.nextLine();
        System.out.println("Você digitou: " + altura + " " + peso);
    }

    public static void main(String[] args) {
        InputExample inputExample = new InputExample();
        inputExample.getImc();

    }
}
