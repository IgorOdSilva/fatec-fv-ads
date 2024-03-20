public class App {
    public static void main(String[] args) throws Exception {
        // System.out.println("Hello, World!");
        // Criando um Objeto - Aluno
        aluno igor = new aluno("Igor", "123456", 2321042, "05/11/2004", "masculino");
        igor.setNome("Igor");
        System.out.println(igor.getNome());

        // Criando outro Objeto na classe - Aluno
        aluno mateus = new aluno();
        mateus.setNome("Mateus");
        System.out.println(mateus.getNome());

    }
}
