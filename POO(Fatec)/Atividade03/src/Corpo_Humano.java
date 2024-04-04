public class Corpo_Humano {
 
    //atributos
    private float massa;
    private float volume;
    private float densidade;
    //atributos desafio
    private float altura;
    private float IMC;
 
    //construtores
    //padrão
    public Corpo_Humano(){
 
    }
 
    //construtor com todos os atributos
    public Corpo_Humano(float massa, float volume, float densidade){
        this.massa = massa;
        this.volume = volume;
        this.densidade = densidade;
    }
 
    //metodo desafio
    void Calc_IMC (float massa, float altura){
        IMC = massa/(altura * altura);
 
    }
 
    //Metodos set e get dos atributos
    public float getmassa(){
        return massa;
    }
 
    public void setmassa(float massa){
        this.massa = massa;
    }
 
    public float getvolume(){
        return volume;
    }
 
    public void setvolume(float volume){
        this.volume = volume;
    }
 
    public float getdensidade(){
        return densidade;
    }
 
    public void setdensidade(float densidade){
        this.densidade = densidade;
    }
 
    public float getaltura(){
        return altura;
    }
 
    public void setAltura(float altura){
        this.altura = altura;
    }
 
    public float IMC(){
        return IMC;
    }
 
    public void setIMC (float IMC){
        this.IMC = IMC;
    }
 
 
 
   
}