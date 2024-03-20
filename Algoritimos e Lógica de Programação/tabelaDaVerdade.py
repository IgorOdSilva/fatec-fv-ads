#-------------------------------------------------------------------------
#Programadores: Igor Oliveira e Mateus Almeida
#Data: 21/09/23
#Tabela da Verdade
#-------------------------------------------------------------------------


#Inicializando Variaveis
cabec = "-"*80
tabela = "-"*50
F = "F"
V = "V"
execucao = True
#--------------------------------------------------------------------------


#Cores e Formatos
Vermelho = '\033[91m'
Verde = '\033[92m'
preto = '\033[30m'
branco = '\033[37m'
fundoBranco = '\033[47m'
Amarelo = '\033[93m'
#--------------------------------------------------------------------------


#Cabeçalho
print(cabec)
print(f'''
 ______     __       __          __       _   __           __        __   
/_  __/__ _/ /  ___ / /__ _  ___/ /__ _  | | / /__ _______/ /__ ____/ /__ 
 / / / _ `/ _ \/ -_) / _ `/ / _  / _ `/  | |/ / -_) __/ _  / _ `/ _  / -_)
/_/  \_,_/_.__/\__/_/\_,_/  \_,_/\_,_/   |___/\__/_/  \_,_/\_,_/\_,_/\__/ 
                                                                          
''')
print(cabec)
#----------------------------------------------------------------------------


#Corpo de Impressão
while execucao:
    P = (input("Olá! Digite o valor lógico(F ou V) para P: "))
    Q = (input("Agora Digite o valor lógico(F ou V) para Q: "))
    R = (input("E por fim Digite o valor lógico(F ou V) para R: "))
    opLog = (int(input("Qual tipo de operador lógico deseja ultilizar? AND(1) ou OR(2): ")))
    if opLog == 1:
        if P in ["V", "v"] and Q in ["V", "v"] and R in ["V", "v"]:
            print(tabela)
            print("|    P   |   Q   |   R   |   P, Q, R (and)       |")
            print(tabela)
            print(f"{P:>6} {Q:>7} {R:>7} {V:>15}")
            print(f"{tabela}")
        else:
            print(tabela)
            print("|    P   |   Q   |   R   |   P, Q, R (and)       |")
            print(tabela)
            print(f"{P:>6} {Q:>7} {R:>7} {F:>15}")
            print(f"{tabela}")
    
    elif opLog == 2:
        if P in ["V", "v"] or Q in ["V", "v"] or R in ["V", "v"]:
            print(tabela)
            print("|    P   |   Q   |   R   |   P, Q, R (or)        |")
            print(tabela)
            print(f"{P:>6} {Q:>7} {R:>7} {V:>15}")
            print(f"{tabela}")
        else:
            print(tabela)
            print("|    P   |   Q   |   R   |   P, Q, R (or)        |")
            print(tabela)
            print(f"{P:>6} {Q:>7} {R:>7} {F:>15}")
            print(f"{tabela}")

    sairContinuar = input("Deseja fazer outra tabela ou sair do programa? Para CONTINUAR(1) Para SAIR(2): ")
    print(cabec)
    if sairContinuar in ["2"]:
        print("Obrigado por ultilizar o programa!")
        execucao = False
        exit
       

    
#----------------------------------------------------------------------------


