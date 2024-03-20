#===========================================================
# Fatec de Ferraz de Vasconcelos
# Disciplina: Algoritmo e Lógica de Programação - ALP
# Professor (a): Luiz Carlos dos Santos Filho
# Programador: Kauan Verissimo da Silva
# Data: 23/10/2023
# Programa: Atividade Avaliativa 02 / Algoritmo e Estrutura de Repetição
# Entrada: 'Entre com o Capital inicial: R$ '
# Saida: 'Segue Tabela'
#==========================================================

# === BIBLIOTECA ===
from os import system
from time import sleep
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# ==== CORES ====
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
ciano = "\033[34m"
cinza = "\033[35m"
fim = "\033[0m"
bold = "\033[1m"

# ==== FERRAMENTA PARA A MANIPULAÇÃO DE STRING ====
A = "-"
B = " "

# === FUNÇÕES ===
def pausa_rotina(msg):
    print(f'\n\n{amarelo}{msg.upper():^109}')
    sleep(1.1)
    print(f'\n{".":^109}')
    sleep(1.1)
    print(f'\n{".":^109}')
    sleep(1.3)
    
# ==== MAIN ====
while True: 
    # VARIÁVEL PARA A CONDIÇÃO DE REPETIÇÃO DO PROGRAMA
    option = 1
    while option == 1:
        
        system('cls')
        sleep(1)
        
        print(f'''{bold}{cinza}   
        ╔═╗┬┌─┐┌┬┐┌─┐┌┬┐┌─┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐┬┌┬┐┌─┐┬  ┬┌─┐┌─┐┌─┐┌─┐┌─┐  ╔═╗┌─┐┌┬┐┌─┐┌─┐┌─┐┌┬┐┌─┐
        ╚═╗│└─┐ │ ├┤ │││├─┤   ││├┤   ║  ├─┤├─┘│ │ ├─┤│  │┌─┘├─┤│  ├─┤│ │  ║  │ ││││├─┘│ │└─┐ │ │ │
        ╚═╝┴└─┘ ┴ └─┘┴ ┴┴ ┴  ─┴┘└─┘  ╚═╝┴ ┴┴  ┴ ┴ ┴ ┴┴─┘┴└─┘┴ ┴└─┘┴ ┴└─┘  ╚═╝└─┘┴ ┴┴  └─┘└─┘ ┴ └─┘ {fim}''')
        sleep(1.3)
        
        # ==== ENTRADA ====
        print(f'\n{bold}{amarelo}{" INSIRA OS DADOS PARA A SIMULAÇÃO ":-^109}{fim}')
        
        # VALIDAÇÃO DA VARIÁVEL ==== C ==== Capital Inicial (Empréstimo)
        while True:
            try:
                C = float(input('\n' + ' ' *38 + 'Entre com o Capital inicial: R$ '))
                
                # VERIFICANDO SE É MAIOR QUE ZERO (0) E IGUAL OU MENOR QUE VINTE MIL REAIS (R$20.000)
                while C <=0 or C >20000:
                    print('\n\n' + f'{A * 49:^109}')
                    print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                    print(B *25 + f'O {bold}Capital inicial{fim} deve ser maior que {bold}R$00.00{fim}, e igual ou menor que {bold}R$20.000')
                    print(f'{A * 49:^109}')
                    C = float(input('\n' + ' ' *38 + 'Entre com o Capital inicial: R$ '))
                
                # QUEBRA DO WHILE TRUE
                if C > 0 and C <= 20000:
                    break
                
            # VERIFICANDO SE DIGITOU ALGUMA LETRA, ESPAÇO EM BRANCO OU ALGUMA PONTUAÇÃO ERRADA
            except ValueError:
                print('\n\n' + f'{A * 58:^109}')
                print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                print(' ' * 25 + f'O {bold}Valor do Emprétimo{fim} está fora dos {bold}parâmetros{fim} de um {bold}numero real{fim}')
                print(f'{A * 58:^109}')
                
        # VALIDAÇÃO DA VARIÁVEL ==== i ==== TAXA DE JUROS NO PERÍODO ESPECIFICADO
        while True:
            try:
                i = float(input(' ' *38 + 'Entre com a taxa de juros (a.m)%: '))
                
                # VERIFICANDO SE É MAIOR QUE ZERO
                while i <=0:
                    print('\n\n' + f'{A * 49:^109}')
                    print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                    print(B *32 + f'O {bold}Valor da Taxa de Juros{fim} deve ser maior que {bold}"0"{fim}')
                    print(f'{A * 49:^109}')
                    i = float(input('\n' + ' ' *38 + 'Entre com a taxa de juros (a.m) %: '))
                
                # QUEBRA DO WHILE TRUE
                if i > 0:
                    break
                
            # VERIFICANDO SE DIGITOU ALGUMA LETRA, ESPAÇO EM BRANCO OU ALGUMA PONTUAÇÃO ERRADA
            except ValueError:
                print('\n\n' + f'{A * 58:^109}')
                print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                print(' ' * 25 + f'O {bold}Valor da Taxa de Juros{fim} está fora dos {bold}parâmetros{fim} de um {bold}numero real{fim}')
                print(f'{A * 58:^109}')
        
        # VALIDAÇÃO DA VARIÁVEL ==== n ==== QUANTIDADE DE PERÍODOS
        while True:
            try:
                n = int(input(' ' *38 + 'Entre com a quantidade de meses que deseja: '))
                
                # VERIFICANDO SE É MAIOR QUE ZERO (0)
                while n <=0:
                    print('\n\n' + f'{A * 49:^109}')
                    print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                    print(B *28 + f'O {bold}Valor da Quantidade de Meses{fim} deve ser maior que {bold}"0"{fim}')
                    print(f'{A * 49:^109}')
                    n = int(input('\n' + ' ' *32 + 'Entre com a quantidade de meses que deseja: '))
                
                # QUEBRA DO WHILE TRUE
                if n > 0:
                    break
                
            # VERIFICANDO SE DIGITOU ALGUMA LETRA, ESPAÇO EM BRANCO OU ALGUMA PONTUAÇÃO ERRADA
            except ValueError:
                print('\n\n' + f'{A * 58:^109}')
                print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                print(' ' * 25 + f'O {bold}Valor da Quantidade de Meses{fim} está fora dos {bold}parâmetros{fim} de um {bold}numero real{fim}')
                print(f'{A * 58:^109}')
                
                
        system('cls')
        pausa_rotina("CALCULANDO")
        
        # ==== CALCULOS ==== SAÍDA PARA O USUÁRIO ====
        
        print(f'{vermelho}{"!!! SEGUE TABELA !!!":-^109}{fim}')
        
        print ('\n'f" {bold} {ciano}                 | {'Mês (meses)':^20} || {'Evolução da dívida':^20} || {'Juros':^20} | ")
        cont = 0 # VARIÁVEL AUXILIAR
        while cont < n :
            if C <= 20000:
                cont = cont + 1
                M = C * (1 + i/100)**cont
                formatted_M = locale.currency(M, grouping=True)
                juros = M - C
                formatted_juros = locale.currency(juros, grouping=True)

            # Saída
            print (f'{ciano}{A:-^109}{fim}')
            print (f"  {bold}                 {amarelo}| {cont:^20} |{verde}| {formatted_M:^20} |{vermelho}| {formatted_juros:^20} | ")
                  
        
        print(f'{vermelho}{A:-^109}{fim}')
        input(f'\n\n {B *32}' + f'{bold}{ciano}Digite{fim} {verde}"ENTER"{fim} {bold}{ciano}para finalizar a simulação{fim}')
        print('\n\n' + f'{vermelho}{A * 58:^109}')
        sleep(1.3)
        
        system('cls')
        
        # ==== PERGUNTANDO SE O USUÁRIO DESEJA REPETIR O PROGRAMA ===='
        
        # VALIDANDO A RESPOSTA DE LOOP DO USUÁRIO
        while True:
            try:
                print(f'{cinza}{A *38:^109}')
                print(f'{B *35}------ Deseja repetir o programa? ------')
                print(f'{B *35}         {amarelo}[1] SIM     {vermelho}[2] NÂO {fim}')
                print(f'{cinza}{A *38:^109}')
                option = int(input(f'\n{B *41}' + 'Digite a opção que deseja: '))
                
                # ==== VALIDAÇÃO DA VARIÁVEL \\\ OPTION /// DENTRO DE 1 E 2 ====
                while option <=0 or option > 2:
                    print(f'\n\n{A *38:^109}')
                    print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                    print(f'{bold}{"Opção selecionada INVÁLIDA":^109}')
                    print(f'{bold}{"Insira uma das opções possíveis":^109}{fim}')
                    
                    
                    # PEDINDO QUE ELE ENTRE COM A INFORMAÇÃO NOVAMENTE
                    print(f'{A *38:^109}')
                    print(f'{B *35}------ Deseja repetir o programa? ------')
                    print(f'{B *35}         {amarelo}[1] SIM     {vermelho}[2] NÂO {fim}')
                    print(f'{A *38:^109}')
                    option = int(input(f'\n{B *41}' + 'Digite a opção que deseja: '))
                    
                # BREAK DE WHILE DE VALIDAÇÃO
                if option == 1 or option == 2:
                    break
                
            # VALIDANDO CASO DIGITE ALGUM CARACTER QUE NÃO SEJA NÚMERO
            except ValueError:
                print('\n\n' + f'{A *55:^109}')
                print(f'{vermelho}{"!!! ERRO ERRO ERRO !!!":-^109}{fim}')
                print(f'{bold}{"Opção digitada fora dos parâmetros de um número inteiro/real":^109}{fim}')
                print(f'{A *55:^109}')
                
        if option == 1:
            pausa_rotina("reiniciando")


            
    # ==== ENCERRAMENTO DO PROGRAMA ====
    pausa_rotina("Fechando o Programa...")  
    
    system('cls')
    
    print(f'''{bold}{amarelo}  
                                ___ ___ __  __ 
                               | __|_ _|  \/  |
                               | _| | || |\/| |
                               |_| |___|_|  |_|{fim}''')  
    break  
    
print() 


