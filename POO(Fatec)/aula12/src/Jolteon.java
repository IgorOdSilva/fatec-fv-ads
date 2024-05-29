public class Jolteon extends Eevee 
{
    @Override
    public String ataque(){
        return "Thunder Shock";
    }
    @Override
    public String defesa(){
        return "Charge";
    }
    @Override
    public String especial(){
        return "Thunder";
    }

    // Construtor
    public Jolteon(String nome, String tipo, Integer altura, Integer hp, double peso){
        super(nome, tipo, altura, hp, peso);
}
}