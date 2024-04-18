public class Funcionario {
    private int id_funcionario;
    private String nome;
    private float salario;

    public Funcionario(int id_funcionario, String nome, float salario) {
        this.id_funcionario = id_funcionario;
        this.nome = nome;
        this.salario = salario;
    }

    public void exibirInformacoes() {
        System.out.println("Id Funcionario: " + id_funcionario);
        System.out.println("Nome: " + nome);
        System.out.println("Salário:" + salario);
    }
}
