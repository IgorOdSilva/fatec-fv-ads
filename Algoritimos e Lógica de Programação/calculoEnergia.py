#----------------------------------------
#Programador: Igor Oliveira
#Data: 28/09/23
#----------------------------------------


#Biblioteca
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#-----------------------------------------------


#Cores e Formatos

#----------------------------------------


#Inicializando Variaveis
cabec = "-"*100
valor = 0
execucao = True
#----------------------------------------


#Cabeçalho
print(cabec)
print('''
   ______      __           __         ______                      _      
  / ____/___ _/ /______  __/ /___     / ____/___  ___  _________ _(_)___ _
 / /   / __ `/ / ___/ / / / / __ \   / __/ / __ \/ _ \/ ___/ __ `/ / __ `/
/ /___/ /_/ / / /__/ /_/ / / /_/ /  / /___/ / / /  __/ /  / /_/ / / /_/ / 
\____/\__,_/_/\___/\__,_/_/\____/  /_____/_/ /_/\___/_/   \__, /_/\__,_/  
                                                         /____/           

''')
print(cabec)
#----------------------------------------


#Entrada e Saída
while execucao:
    nomeUser = input("Olá! Por favor digite seu nome: ")
    consumo = float(input(f"Olá {nomeUser}, informe a quantidade de kWh consumida:  "))
    tipoInstalacao = input(f"{nomeUser} agora informe o tipo de instalação. R para Residencial; I para Industrial; C para Comercial: ")
    print(cabec)


    if tipoInstalacao in ["R", "r"]:
        if consumo <= 500:
            precoConsumo = 0.40
            valorConta = consumo*precoConsumo
            valorContaFormatado = locale.currency(valorConta, grouping=True)
            print(f"O valor da sua conta será: {valorContaFormatado}")
        elif consumo > 500:
            precoConsumo = 0.65
            valorConta = consumo*precoConsumo
            valorContaFormatado = locale.currency(valorConta, grouping=True)
            print(f"O valor da sua conta será: {valorContaFormatado}")
    elif tipoInstalacao in ["I", "i"]:
        if consumo <= 1000:
            precoConsumo = 0.55
            valorConta = consumo*precoConsumo
            valorContaFormatado = locale.currency(valorConta, grouping=True)
            print(f"O valor da sua conta será: {valorContaFormatado}")
        elif consumo > 1000:
            precoConsumo = 0.60
            valorConta = consumo*precoConsumo
            valorContaFormatado = locale.currency(valorConta, grouping=True)
            print(f"O valor da sua conta será: {valorContaFormatado}")
    elif tipoInstalacao in ["C", "c"]:
        if consumo <= 5000:
            precoConsumo = 0.55
            valorConta = consumo*precoConsumo
            valorContaFormatado = locale.currency(valorConta, grouping=True)
            print(f"O valor da sua conta será: {valorContaFormatado}")
        elif consumo > 5000:
            precoConsumo = 0.60
            valorConta = consumo*precoConsumo
            valorContaFormatado = locale.currency(valorConta, grouping=True)
            print(f"O valor da sua conta será: {valorContaFormatado}")
    print(cabec)
    print("Sua conta foi calculada seguindo os seguintes valores:")
    print(''' 
         _____________________________________________________________________________
        | Preço por tipo de faixa de consumo                                          |
        |_____________________________________________________________________________|
        | Tipo         |   Faixa (kWh)          |   Preço por kWh                     |
        |______________|________________________|_____________________________________|
        | Residencial  |   Até 500 (inclusive)  |   R$ 0,40 Acima de 500 R$ 0,65      |
        |______________|________________________|_____________________________________|
        | Comercial    |   Até 1000 (inclusive) |   R$ 0,55 Acima de 1000 R$ 0,60     |
        |______________|________________________|_____________________________________|
        |Industrial    |  Até 5000 (inclusive)  |  R$ 0,55 Acima de 5000 R$ 0,60      |
        |______________|________________________|_____________________________________|
    ''')

    sairContinuar = input("Deseja simular outro valor ou sair do programa? Para CONTINUAR(1) Para SAIR(2): ")
    print(cabec)
    if sairContinuar in ["2"]:
        print("Obrigado por ultilizar o programa!")
        execucao = False
        exit

#----------------------------------------
