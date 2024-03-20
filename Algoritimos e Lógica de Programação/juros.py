#----------------------------------------
#Programador Igo Oliveira
#Data 17/10/2023
#Programa Evolução de Divida
#----------------------------------------

#Biblioteca-----------------------------
import os
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#----------------------------------------

#Cores-----------------------------------
cor_vermelha = "\033[31m"
cor_amarela = "\033[33m"
cor_fim = "\033[0m"
verde = "\033[32m"
#----------------------------------------

#TRATAMENTO DE ERRO---------------------------------------------------------------------------
def obter_valor(mensagem, min_valor, max_valor):
    while True:
        try:
            valor = float(input(mensagem))
            if min_valor <= valor <= max_valor:
                return valor
            else:
                print(f'\n{cor_vermelha}Valor deve estar entre {min_valor} e {max_valor}.{cor_fim}')
        except ValueError:
            print(f'\n{cor_vermelha}Valor digitado não é válido.{cor_fim}')
#-----------------------------------------------------------------------------------------------------

#CALCULO----------------------------------------------------------------------------------------------
def calcular_evolucao_divida(C, i, n):
    evolucao_divida = []
    for mes in range(1, n + 1):
        M = C * (1 + i / 100) ** mes
        juros = M - C
        evolucao_divida.append((mes, M, juros))
    return evolucao_divida
#-----------------------------------------------------------------------------------------------------

#FORMATAÇÃO TABELA------------------------------------------------------------------------------------
def exibir_tabela(evolucao_divida):
    print(f'\n{verde}{"Mês (meses)":^15}{cor_fim} | {cor_amarela}{"Evolução da Dívida (R$)":^25}{cor_fim} | {cor_vermelha}{"Juros (R$)":^15}{cor_fim}')
    print("-" * 65)
    for mes, montante, juros in evolucao_divida:
        formatted_montante = locale.currency(montante, grouping=True)
        formatted_juros = locale.currency(juros, grouping=True)
        print(f'{verde}{mes:^15}{cor_fim} | {cor_amarela}{formatted_montante:^25}{cor_fim}  | {cor_vermelha}{formatted_juros:^15}{cor_fim}')
#-----------------------------------------------------------------------------------------------------


#ENTRADA DE DADOS-------------------------------------------------------------------------------------
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
  _____            _            /\/|             _        ____  _       _     _       
 | ____|_   _____ | |_   _  ___|/\/_  ___     __| | ___  |  _ \(_)_   _(_) __| | __ _ 
 |  _| \ \ / / _ \| | | | |/ __/ _` |/ _ \   / _` |/ _ \ | | | | \ \ / / |/ _` |/ _` |
 | |___ \ V / (_) | | |_| | (_| (_| | (_) | | (_| |  __/ | |_| | |\ V /| | (_| | (_| |
 |_____| \_/ \___/|_|\__,_|\___\__,_|\___/   \__,_|\___| |____/|_| \_/ |_|\__,_|\__,_|
                            )_)                                                       
          ''')

    while True:
        C = obter_valor("Informe o valor do empréstimo (R$): ", 0, 20000)
        i = obter_valor("Informe a taxa de juros mensal (%): ", 0, 100)
        n = int(obter_valor("Informe a quantidade de meses: ", 1, float('inf')))

        evolucao_divida = calcular_evolucao_divida(C, i, n)

        exibir_tabela(evolucao_divida)

        repetir = input("Deseja realizar outra simulação? (S/N): ")
        if repetir.strip().lower() != 's':
            os.system('clear')
            break

if __name__ == "__main__":
    main()
#-----------------------------------------------------------------------------------------------------



