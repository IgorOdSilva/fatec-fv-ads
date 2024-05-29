public class FolhaPGTO {
    public static void main(String[] args) throws Exception {
        Mensalista men1, men2;
        Horista hora1, hora2;

        // Empregados mensalistas 
        men1 = new Mensalista("jose", "Rua da fatec", 0, "junior");
        men1.calcularSalario();
        men1.calcINSS();
        men1.Imprimir();
        

        men2 = new Mensalista("ana", "Rua com fim", 0, "Pleno");
        men2.calcularSalario();
        men2.calcINSS();
        men2.Imprimir();
        
        //Empregados horistas        
        hora1= new Horista("Carlos", "Rua abc", 0,20);
        hora1.calcularSalario();
        hora1.Imprimir();

        hora2 = new Horista("Cristina", "Rua do Centro", 0, 100);
        hora2.Imprimir();
        
    }
}