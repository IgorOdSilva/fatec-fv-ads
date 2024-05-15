import java.util.Scanner;

public class Funcionario {
    private String nome;
    private String cpf;
    private double salario;
    private String cargo;
    private String data_nascimento;

    public Funcionario(String nome, String cpf, double salario, String cargo, String data_nascimento){
        this.nome = nome;
        this.cpf = cpf;
        this.salario = salario;
        this.cargo = cargo;
        this.data_nascimento = data_nascimento;
    }

    public String infoFuncionario(String nome, String cpf, double salario, String cargo, String data_nascimento){
        return "Nome: " + this.nome + "\nCPF: " + this.cpf + "\nSalário: " + this.salario + "\nCargo: " + this.cargo + "\nData de Nascimento: " + this.data_nascimento;
    }
    
     public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Mostra Funcionario");
        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();
        
        System.out.print("Digite seu CPF: ");
        String cpf = scanner.nextLine();
        
        System.out.print("Digite seu Cargo: ");
        String cargo = scanner.nextLine();

        System.out.print("Digite seu Salário: ");
        double salario = scanner.nextDouble();

        System.out.print("Digite sua Data de Nascimento: ");
        String data_nascimento = scanner.nextLine();

        Funcionario newFuncionario = new Funcionario(nome, cpf, salario, cargo, data_nascimento);

        String resultadoFuncionario = newFuncionario.infoFuncionario(nome, cpf, salario, cargo, data_nascimento);

        System.out.println("Funcionario Cadastrado!");
        System.out.println(resultadoFuncionario);

        scanner.close();
    }
}