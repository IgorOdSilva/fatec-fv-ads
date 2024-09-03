public class Funcionario {
    private String nome;
    private Float salario;

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public Float getSalario() {
        return salario;
    }
    public void setSalario(Float salario) {
        this.salario = salario;
    }

    public Float calcularINSS(){
        float desconto=0;
        if (salario<=1419.00){
            desconto = salario*0.075f;
        }else if (salario>1419.00 && salario<=2666.68){
            desconto = salario*0.09f;
        
        }else if (salario>2666.68 && salario<=4000.00){
            desconto = salario*0.12f;
        }else if (salario>4000.00 && salario<=7786.02){
            desconto = salario*0.14f;
        }else{
            desconto = 7786.02f*0.14f;
        }

        return desconto;

    }


}
