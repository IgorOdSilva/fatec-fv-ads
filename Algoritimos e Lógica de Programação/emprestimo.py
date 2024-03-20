#-----------------------------------------------
#Programador Igor Oliveira
#Data 19/09/23
#Emprestimo Bancário Imóvel
#-----------------------------------------------


#Cores e Formatos
BOLD    = "\033[;1m"
Azul = '\033[94m'
Vermelho = '\033[91m'
Amarelo = '\033[93m'
CYAN  = "\033[1;36m"
Fim = '\033[0m'
GREEN = "\033[0;32m"

#-----------------------------------------------

#Biblioteca
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#-----------------------------------------------

#Inicializando Variaveis
cabec = ("=")*100
execucao = True
#-----------------------------------------------

#Cabeçalho
print(cabec)
print(f'''{CYAN}
  _____                       __      _   _                   ___             __           _ 
 | ____|_ __ ___  _ __  _ __ /_/  ___| |_(_)_ __ ___   ___   |_ _|_ __ ___   /_/__   _____| |
 |  _| | '_ ` _ \| '_ \| '__/ _ \/ __| __| | '_ ` _ \ / _ \   | || '_ ` _ \ / _ \ \ / / _ \ |
 | |___| | | | | | |_) | | |  __/\__ \ |_| | | | | | | (_) |  | || | | | | | (_) \ V /  __/ |
 |_____|_| |_| |_| .__/|_|  \___||___/\__|_|_| |_| |_|\___/  |___|_| |_| |_|\___/ \_/ \___|_|
                 |_|                                                                                                                                                                                          
{Fim}
''')
print(cabec)
#-----------------------------------------------


#Entrada Valores
while execucao:
  nome = input("Olá! Para começar primeiro nos informe seu nome: ")
  valorImovel = float(input(f"Olá " + nome + ", qual valor do imóvel(em R$) que deseja adquirir? "))
  valorImovelFormatado = locale.currency(valorImovel, grouping=True)
  print(valorImovelFormatado)
  salario = float(input(f"" + nome + ", agora digite seu salário BRUTO(em R$), ex 1320: " ))
  salFormatado = locale.currency(salario, grouping=True)
  print(salFormatado)
  nParcelas = int(input(f"Em quantos meses deseja pagar? OBS: No máximo 240. "))
  print(f" {nParcelas}  meses")
  print(cabec)

  # Verifica se a quantidade de meses está dentro do limite
  if nParcelas > 240:
      print(f"{Vermelho}Empréstimo não aprovado. A quantidade de meses excede o limite máximo (240 meses).{Fim}")
      print(cabec)
  else:
      # Calcula o valor da prestação mensal
      prestacaoMensal = valorImovel / nParcelas
      prestacaoMensalFormatado = locale.currency(prestacaoMensal, grouping=True)

      # Verifica se a prestação mensal não excede 30% do salário bruto
      if prestacaoMensal > 0.3 * salario:
          print(f"{Vermelho}Empréstimo não aprovado. A prestação mensal excede 30% do salário bruto.{Fim}")
          print(cabec)

          # Calcula o salário necessário para adquirir o imóvel com a quantidade de meses informada
          salarioNecessario = valorImovel / (0.3 * nParcelas)
          salarioNecessarioFormatado = locale.currency(salarioNecessario, grouping=True)
          print(f"Para adquirir o imóvel em {nParcelas} meses, o salário necessário é de R$ {salarioNecessarioFormatado}.")

          # Calcula a quantidade mínima de meses necessários para adquirir o imóvel com o salário informado
          mesesNecessarios = valorImovel / (0.3 * salario)
          print(f"Com um salário de R$ {salFormatado}, você precisaria de pelo menos {int(mesesNecessarios)} meses para adquirir o imóvel.")
      else:
          print(f"{GREEN}Empréstimo aprovado!{Fim}")
          print(cabec)
          print(f"Condições do empréstimo:")
          print(cabec)
          print(f"Valor da prestação mensal: R$ {prestacaoMensalFormatado}")
          print(f"Número de meses solicitado: {nParcelas} meses")
          print(cabec)

  sairContinuar = input("Deseja fazer outra simular outro empréstimo ou sair do programa? Para CONTINUAR(1) Para SAIR(2): ")
  print(cabec)
  if sairContinuar in ["2"]:
    print("Obrigado por ultilizar o programa!")
    execucao = False
    exit
       

#-----------------------------------------------

