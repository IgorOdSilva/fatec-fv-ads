public class Operadores {
 
    // Operadores comuns
    public float adicao(float v1, float v2) {
        return v1 + v2;
    }
 
    public float subtracao(float v1, float v2) {
        return v1 - v2;
    }
 
    public float multiplicacao(float v1, float v2) {
        return v1 * v2;
    }
 
    public float divisao(float v1, float v2) {
        return v1 / v2;
    }
 
    // Operadores de Atribuição
    public float atribuicaoSoma(float v1, float v2) {
        return v1 += v2;
    }
 
    public float atribuicaoSubtracao(float v1, float v2) {
        return v1 -= v2;
    }
 
    public float atribuicaoMultiplicacao(float v1, float v2) {
        return v1 *= v2;
    }
 
    public float atribuicaoDivisao(float v1, float v2) {
        return v1 /= v2;
    }
 
    // Operadores Lógicos
    public boolean AND(boolean v1, boolean v2) {
        return v1 && v2;
    }
 
    public boolean OR(boolean v1, boolean v2) {
        return v1 || v2;
    }
 
    public boolean NOT(boolean v) {
        return !v;
    }
 
    // Operadores de Comparação
    public boolean igual(float v1, float v2) {
        return v1 == v2;
    }
 
    public boolean diferente(float v1, float v2) {
        return v1 != v2;
    }
 
    public boolean maiorQue(float v1, float v2) {
        return v1 > v2;
    }
 
    public boolean maiorOuIgualA(float v1, float v2) {
        return v1 >= v2;
    }
 
    public boolean menorQue(float v1, float v2) {
        return v1 < v2;
    }
 
    public boolean menorOuIgualA(float v1, float v2) {
        return v1 <= v2;
    }
}