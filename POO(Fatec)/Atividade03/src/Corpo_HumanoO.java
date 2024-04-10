public class Corpo_HumanoO{
    public static void main(String[] args) {
 
        //Objeto exercicio
        Corpo_Humano c1 = new Corpo_Humano();
        c1.setmassa(2f);
 
        //Objeto desafio
        Corpo_Humano cD = new Corpo_Humano();
        cD.setmassa(76f);
        cD.setvolume(80f);
        cD.setdensidade(40f);
        cD.setAltura(1.75f);
             
 
        cD.Calc_IMC(cD.getmassa(), cD.getaltura());
       
        System.out.println("Seu IMC é: " + cD.IMC() + "\n" + "O IMC foi calculado fazendo a Massa Dividida pela Altura");
 
       
    }
   
}
