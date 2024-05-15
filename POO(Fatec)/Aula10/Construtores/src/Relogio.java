public class Relogio {
    private int hora;
    private int minuto;
    private int segundo;

    // Construtor
    public Relogio(){

    }

    // Tradicional com os atributos
    public Relogio(int hora, int minuto, int segundo){
        this.hora = hora;
        this.minuto = minuto;
        this.segundo = segundo;
    }

    // 2 versão: Inserindo apenas hora e segundo
    public Relogio(int hora, int minuto){
        this.hora = hora;
        this.minuto = minuto;
        this.segundo = 0;
    }

    // 3 versão: Inserindo apenas a hora
    public Relogio(int hora) {
        this.hora = hora;
        this.minuto = 0;
        this.segundo = 0;
    }

    public int getHora() {
        return hora;
    }

    public void setHora(int hora) {
        this.hora = hora;
    }

    public int getMinuto() {
        return minuto;
    }

    public void setMinuto(int minuto) {
        this.minuto = minuto;
    }

    public int getSegundo() {
        return segundo;
    }

    public void setSegundo(int segundo) {
        this.segundo = segundo;
    }
}