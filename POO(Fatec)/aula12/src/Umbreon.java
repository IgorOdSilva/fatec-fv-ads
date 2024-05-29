public class Umbreon extends Eevee {
    @Override
    public String ataque(){
        return "Assurance";
    }
    @Override
    public String defesa(){
        return "Sand Attack";
    }
    @Override
    public String especial(){
        return "Dark Pulse";
    }

    // Construtor
    public Umbreon(String nome, String tipo, Integer altura, Integer hp, double peso){
        super(nome, tipo, altura, hp, peso);
}
}
