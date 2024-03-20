public class aluno {
    private String nome;
    private String cpf;
    private int rm;
    private String dataDeNascimento;
    private String sexo;

    public void setNome(String entrada){
        this.nome = entrada;
    }

    public void setRm(int entrada){
        this.rm = entrada;
    }

    public String getNome(){
        return this.nome;
    }

    public int getRm(){
        return this.rm;
    }

    // Construtor Versão1
    public aluno(String nome, String cpf, int rm, String dataDeNascimento, String sexo){
        this.nome = nome;
        this.cpf = cpf;
        this.rm = rm;
        this.dataDeNascimento = dataDeNascimento;
        this.sexo = sexo;
    }

    // Contrutor Versão2
    public aluno(){

    }

} 

