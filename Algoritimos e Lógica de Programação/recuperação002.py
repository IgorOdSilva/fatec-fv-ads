import os
import time
import locale

# Configuração da localização para formato de moeda em reais
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Definição das cores
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
ciano = "\033[34m"
cinza = "\033[35m"
fim = "\033[0m"
bold = "\033[1m"
A = ""
B = ""

# Função para pausar a rotina com mensagens
def pausa_rotina(msg):
    print(f'\n\n{amarelo}{msg.upper():^109}')
    time.sleep(1.1)
    print(f'\n{".":^109}')
    time.sleep(1.1)
    print(f'\n{".":^109}')
    time.sleep(1.3)

# Função para solicitar um valor válido
def obter_valor(mensagem, min_valor, max_valor):
    while True:
        try:
            valor = float(input(mensagem))
            if min_valor <= valor <= max_valor:
                return valor
            else:
                print('\n' + A * 49)
                print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                print(f'{B * 25}O valor deve estar entre {min_valor} e {max_valor}')
                print(A * 49)
        except ValueError:
            print('\n' + A * 58)
            print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
            print(f'{B * 25}Valor digitado não é um número real válido')
            print(A * 58)

# Função para calcular o empréstimo
def calcular_emprestimo(C, i, n):
    resultados = []
    for cont in range(1, n + 1):
        M = C * (1 + i / 100) ** cont
        juros = M - C
        resultados.append((cont, M, juros))
    return resultados

# Função para exibir a tabela de resultados
def exibir_tabela(resultados):
    print(f'{vermelho}{"!!! SEGUE TABELA !!!":-^109}{fim}')
    print('\n'f" {bold} {ciano}                 | {'Mês (meses)':^20} || {'Evolução da dívida':^20} || {'Juros':^20} | ")
    for cont, M, juros in resultados:
        formatted_M = locale.currency(M, grouping=True)
        formatted_juros = locale.currency(juros, grouping=True)
        print(f'{ciano}{A:-^109}{fim}')
        print(f"  {bold}                 {amarelo}| {cont:^20} |{verde}| {formatted_M:^20} |{vermelho}| {formatted_juros:^20} | ")

# Função principal
def main():
    while True:
        os.system('cls')
        time.sleep(1)
        
        print(f'''{bold}{cinza}   
        ╔═╗┬┌─┐┌┬┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐┬┌┬┐┌─┐┬  ┬┌─┐┌─┐┌─┐┌─┐┌─┐  ╔═╗┌─┐┌┬┐┌─┐┌─┐┌─┐┌┬┐┌─┐
        ╚═╗│└─┐ │ ├┤ │││├─┤   ││├┤   ║  ├─┤├─┘│ │ ├─┤│  │┌─┘├─┤│  ├─┤│ │  ║  │ ││││├─┘│ │└─┐ │ │ │
        ╚═╝┴└─┘ ┴ └─┘┴ ┴┴ ┴  ─┴┘└─┘  ╚═╝┴ ┴┴  ┴ ┴ ┴ ┴┴─┘┴└─┘┴ ┴└─┘┴ ┴└─┘  ╚═╝└─┘┴ ┴┴  └─┘└─┘ ┴ └─┘ {fim}''')
        time.sleep(1.3)
        
        print(f'\n{bold}{amarelo}{" INSIRA OS DADOS PARA A SIMULAÇÃO ":-^109}{fim}')
        
        C = obter_valor(' ' * 38 + 'Entre com o Capital inicial: R$ ', 0, 20000)
        i = obter_valor(' ' * 38 + 'Entre com a taxa de juros (a.m)%: ', 0, float('inf'))
        n = obter_valor(' ' * 38 + 'Entre com a quantidade de meses que deseja: ', 1, float('inf'))
        
        os.system('cls')
        pausa_rotina("CALCULANDO")
        
        resultados = calcular_emprestimo(C, i, n)
        exibir_tabela(resultados)
        
        os.system('cls')
        
        while True:
            try:
                print(f'{cinza}{A * 38:^109}')
                print(f'{B * 35}------ Deseja repetir o programa? ------')
                print(f'{B * 35}         {amarelo}[1] SIM     {vermelho}[2] NÃO {fim}')
                print(f'{cinza}{A * 38:^109}')
                option = int(input(f'\n{B * 41}' + 'Digite a opção que deseja: '))
                
                while option < 1 or option > 2:
                    print(f'\n\n{A * 38:^109}')
                    print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                    print(f'{bold}{"Opção selecionada INVÁLIDA":^109}')
                    print(f'{bold}{"Insira uma das opções possíveis":^109}{fim}')
                    print(f'{A * 38:^109}')
                    option = int(input(f'\n{B * 41}' + 'Digite a opção que deseja: '))
                
                if option == 1 or option == 2:
                    break
            except ValueError:
                print('\n' + A * 55)
