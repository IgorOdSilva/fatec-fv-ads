public class Horista extends Empregado{
    private double horas;

    // Construtor
    public Horista(String nome, String endereço, double salario, double horas) {
        super(nome,endereço,salario);
        this.horas = horas;
}

// mmetodos de acesso
   public void set_horas (double h) {
    horas = h;
   }

   public double get_horas() {
    return horas;
   }

   public void calcularSalario() {
    salario = horas * 50;
   }
}
