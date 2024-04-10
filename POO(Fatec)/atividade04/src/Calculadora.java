public class Calculadora {
    public static void main(String[] args) {
        Operadores op = new Operadores();
 
        // operações matemáticas
        System.out.println("Resultado da Adição: " + op.adicao(10, 5));
        System.out.println("Resultado da Subtração: " + op.subtracao(10, 5));
        System.out.println("Resultado da Multiplicação: " + op.multiplicacao(10, 5));
        System.out.println("Resultado da Divisão: " + op.divisao(10, 5));
 
        // operações lógicas
        boolean a = true;
        boolean b = false;
        System.out.println("Resultado do AND lógico: " + op.AND(a, b));
        System.out.println("Resultado do OR lógico: " + op.OR(a, b));
        System.out.println("Resultado do NOT lógico para a: " + op.NOT(a));
 
        // operações de comparação
        float x = 10;
        float y = 5;
        System.out.println("x é igual a y? " + op.igual(x, y));
        System.out.println("x é diferente de y? " + op.diferente(x, y));
        System.out.println("x é maior que y? " + op.maiorQue(x, y));
        System.out.println("x é maior ou igual a y? " + op.maiorOuIgualA(x, y));
        System.out.println("x é menor que y? " + op.menorQue(x, y));
        System.out.println("x é menor ou igual a y? " + op.menorOuIgualA(x, y));
 
        // operações de atribuição
        float valor1 = 10;
        float valor2 = 5;
        System.out.println("Valor inicial de valor1: " + valor1);
        System.out.println("Valor inicial de valor2: " + valor2);
        valor1 = op.atribuicaoSoma(valor1, valor2);
        System.out.println("Após atribuição de soma, valor de valor1: " + valor1);
        valor2 = op.atribuicaoSubtracao(valor2, valor1);
        System.out.println("Após atribuição de subtração, valor de valor2: " + valor2);
        valor1 = op.atribuicaoMultiplicacao(valor1, valor2);
        System.out.println("Após atribuição de multiplicação, valor de valor1: " + valor1);
        valor2 = op.atribuicaoDivisao(valor2, valor1);
        System.out.println("Após atribuição de divisão, valor de valor2: " + valor2);
    }
}
