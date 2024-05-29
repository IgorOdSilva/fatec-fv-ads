public class Espeon extends Eevee {
    @Override
    public String ataque(){
        return "Psybeam";
    }
    @Override
    public String defesa(){
        return "Tail Whip";
    }
    @Override
    public String especial(){
        return "Psychic";
    }

    // Construtor
    public Espeon(String nome, String tipo, Integer altura, Integer hp, double peso){
        super(nome, tipo, altura, hp, peso);
}
}
