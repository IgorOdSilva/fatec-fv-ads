public class Glaceon extends Eevee {
    @Override
    public String ataque(){
        return "Ice Shard";
    }
    @Override
    public String defesa(){
        return "Snowscape";
    }
    @Override
    public String especial(){
        return "Blizzard";
    }

    // Construtor
    public Glaceon(String nome, String tipo, Integer altura, Integer hp, double peso){
        super(nome, tipo, altura, hp, peso);
}
}
