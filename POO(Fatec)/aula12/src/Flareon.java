public class Flareon extends Eevee {
    @Override
    public String ataque(){
        return "Fire Fang";
    }
    @Override
    public String defesa(){
        return "Endure";
    }
    @Override
    public String especial(){
        return "Flamethrower";
    }

    // Construtor
    public Flareon(String nome, String tipo, Integer altura, Integer hp, double peso){
        super(nome, tipo, altura, hp, peso);
}
}
