import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        // Declarando um Array Unidimessional
        int[] meu_array = new int[5];

        // Inicializando os valores por acesso rápido

        // Na posição 0 estou guardando o elemento 10
        meu_array[0] = 10;
        meu_array[1] = 20;
        meu_array[2] = 30;
        meu_array[3] = 40;
        meu_array[4] = 50;

        // recuperar os elementos da array por Acesso Rápido
        int element_0 = meu_array[2];
        int element_1 = meu_array[4];

        System.out.println(element_0 + " " + element_1);

        // Array (ou Vetor) do tipo Texto/String
        // A quantidade de elementos é amarrada no inicio, por meio de um numero inteiro
        // Permitindo que a mesma seja ampliada/diminuida no decorrer do processo
        String[] lista_aluno = new String[5];

        lista_aluno[0] = "João";
        lista_aluno[1] = "Vanessa";
        lista_aluno[2] = "Davi";
        lista_aluno[3] = "Lucas";
        lista_aluno[4] = "Igor";

        // Acesso Direto (ou Rápido)
        System.out.println(lista_aluno[2]);

        // Array (ou Vetor) do tipo Texto/String
        // A quantidade de elementos é amarrada no ato da criação por meio dos conteúdos
        // Portanto, não é possível modificar a quantidade, somente adicionando e
        // removendo elementos

        String[] lista_cidades = { "Poá", "Itaim Paulista",
                "Suzano", "Itu" };

        // 0- Poá 1-Itam Paulista 2-Suzano 3-Itua

        // Acesso Direto (ou Rápido)
        System.out.println(lista_cidades[2]);

        // Acesso Posicional - Sequencial (Percorrer um Array)
        for (int i = 0; i < lista_aluno.length; i++) {
            System.out.println("Elemento " + i + ":" + lista_aluno[i]);
        }

        // Acesso Posicional - Sequencial (Percorrer um Array)
        for (int i = 0; i < lista_cidades.length; i++) {
            System.out.println("Elemento " + i + ":" + lista_cidades[i]);
        }

        //Exibindo uma Array dentro de um SysOut
        int[] array = {10,20,30,40,50};
        System.out.println(Arrays.toString(array));
        System.out.println(Arrays.toString(lista_cidades));


        //Verificando o Tamanho da Array

        System.out.println("O Tamanho é: "+array.length);
        System.out.println("O Tamanho é: "+lista_cidades.length);

        //copiando uma Array

        int[] copia = array.clone();
        String[] copia_cidade = lista_cidades.clone();
        String[] copia_cidade2 = lista_cidades;

        System.out.println("Copia: "+ Arrays.toString(copia));
        System.out.println("Copia: "+ Arrays.toString(copia_cidade));


        //recortando e copiando para uma nova array
        String[] copia_sel = Arrays.copyOf(lista_cidades, 2);

        
        System.out.println("Copia: "+ Arrays.toString(copia_sel));

        //organizando elementos 
        int[] nova_array = {5,6,4,2,3,1,0};
        Arrays.sort(nova_array);

        System.out.println("Ordenada em: "+ Arrays.toString(nova_array));
        

        //inserindo um valor igual em todas as posições

        int[] array_vazia = new int[5];
     
        System.out.println(":"+ Arrays.toString(array_vazia));
     
        Arrays.fill(array_vazia,10);

        System.out.println(":"+ Arrays.toString(array_vazia));
        
        //verificando se as arrays são iguais
        boolean resp = Arrays.equals(lista_cidades, copia_cidade);

        System.out.println("São iguais: "+resp);

        //testando com o if
        if(Arrays.equals(lista_cidades,copia_cidade)){
            System.out.println("Elas são iguais");
        }else{
            System.out.println("Elas são diferentes");
        }
        // buscando elementos
        int posicao = Arrays.binarySearch(array,30 );
        System.out.println("Foi localizado na posicao: "+posicao);
    }
}
