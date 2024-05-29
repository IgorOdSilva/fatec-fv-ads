public class Sylveon extends Eevee {
    @Override
    public String ataque(){
        return "Draining Kiss";
    }
    @Override
    public String defesa(){
        return "Charm";
    }
    @Override
    public String especial(){
        return "Moonblast";
    }

    // Construtor
    public Sylveon(String nome, String tipo, Integer altura, Integer hp, double peso){
        super(nome, tipo, altura, hp, peso);
}
}
