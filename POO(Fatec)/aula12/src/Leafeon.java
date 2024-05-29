public class Leafeon extends Eevee {
    @Override
    public String ataque(){
        return "Quick Attack";
    }
    @Override
    public String defesa(){
        return "Leech Seed";
    }
    @Override
    public String especial(){
        return "Magical Leaf";
    }

    // Construtor
    public Leafeon(String nome, String tipo, Integer altura, Integer hp, double peso){
        super(nome, tipo, altura, hp, peso);
}
}
