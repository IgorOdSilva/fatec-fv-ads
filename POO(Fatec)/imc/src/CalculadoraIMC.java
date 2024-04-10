import java.util.Scanner;

public class CalculadoraIMC {
    private double peso;
    private double altura;

    public CalculadoraIMC(double peso, double altura) {
        this.peso = peso;
        this.altura = altura;
    }

    public double calcularIMC() {
        return peso / (altura * altura);
    }

    public String interpretarResultado(double imc) {
        if (imc < 18.5) {
            return "Abaixo do peso";
        } else if (imc < 25) {
            return "Peso normal";
        } else if (imc < 30) {
            return "Sobrepeso";
        } else {
            return "Obesidade";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Calculadora de IMC");
        System.out.print("Digite seu peso em kg: ");
        double peso = scanner.nextDouble();
        
        System.out.print("Digite sua altura em metros: ");
        double altura = scanner.nextDouble();

        CalculadoraIMC calculadora = new CalculadoraIMC(peso, altura);
        double imc = calculadora.calcularIMC();
        String resultado = calculadora.interpretarResultado(imc);

        System.out.println("Seu IMC é: " + imc);
        System.out.println("Você está classificado como: " + resultado);

        scanner.close();
    }
}
