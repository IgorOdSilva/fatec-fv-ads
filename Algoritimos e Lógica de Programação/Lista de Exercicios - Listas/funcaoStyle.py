import os

def print_centralizado(texto):
    # Obtém a largura da tela
    largura_tela = os.get_terminal_size().columns
    
    # Calcula a margem esquerda para centralizar o texto
    margem_esquerda = (largura_tela - len(texto)) // 2
    
    # Imprime o texto com a margem adequada
    print(' ' * margem_esquerda + texto)
