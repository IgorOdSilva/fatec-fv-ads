public class Eevee {
    private String nome;
    private String tipo;
    private int altura, hp;
    private double peso;
 
 public String ataque(){
    return "Tackle";
 }
 
 public String defesa(){
    return "Growl";
 }
 
 public String especial(){
    return "Bite";
 }
 
 // Metodo Get e Set
public String getNome() {
    return nome;
}

public void setNome(String Nome) {
    this.nome = nome;
}

 public String getTipo() {
    return tipo;
}
public void setTipo(String Tipo) {
    this.tipo = tipo;
}
public Integer getAltura() {
    return altura;
}
public void setAltura(Integer Altura) {
    this.altura = altura;
}
public Integer getHp() {
    return hp;
}
public void setHp(Integer Hp) {
    this.hp = hp;
}
 
public double getPeso() {
    return peso;
}
 
public void setPeso(double peso) {
    this.peso = peso;
}
 
// Construtor
public Eevee(String nome, String tipo, int altura, int hp, double peso ) {
this.nome = nome;
this.tipo = tipo;
this.altura = altura;
this.hp = hp;
this.peso = peso;
}

// Metodo Imprimir
public void imprimir(){
System.out.println("Eu sou: " + getNome());
System.out.println("Tipo: " + getTipo());
System.out.println("Altura: " + getAltura() + "Cm");
System.out.println("HP: " + getHp());
System.out.println("Peso: " + getPeso() + "Kg");
System.out.println("Ataque: " + ataque());
System.out.println("Ataque Especial: " + especial());
System.out.println("Defesa: " + defesa());
System.out.println("\n");
}
}