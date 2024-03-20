#----------------------------------------
#Programador Igor Oliveira
#Data 17/11/2023
#Crud
#----------------------------------------
 
 
#Biblioteca------------------------------
import os
import funcaoLoad as FC

#----------------------------------------
 
 
#Inicializando Variaveis
execucao = True
L1 = {}
L1 = FC.Load_Txt()
cabec = "_"*150
#----------------------------------------
 
 
#Programa-------------------------------
       
while True:
    print ('''
________________________________________
Consulta Paciente
________________________________________
Escolha uma opção do Menu:
________________________________________
[1] Cadastrar Paciente
[2] Pesquisar Paciente
[3] Editar
[4] Excluir
[5] Pesquisa Avançada de Paciente
[6] Finalizar
 
''')
    opt = input("Escolha opção desejada:")
    os.system('cls')
    if  opt == "1": #Inclusão de Registros
        print(cabec)
        print("Cadastro de Pacientes")
        print(cabec)
        print("\n")
        cpf=input("Entre com o número do seu CPF(somente números): ")
        if cpf in L1:
            print ("Cadastro já existe.")
        else:
            nome = input("Entre com o nome: ")
            idade = input("Entre com a sua data de nascimento EX(17/03/2004): ")
            cartaoSus = input("Entre com o seu cartão do SUS: ")
            cidade = input("Informe a cidade que você mora: ")
            L1[cpf] = [nome, idade, cartaoSus, cidade]
            print ('Registro Incluído')
            FC.Save_Cadastro(L1)
            input ("Digite enter para voltar ao menu")
            os.system ('cls')
    elif opt == "2":  # Pesquisar Consultas
        print(cabec)
        print("Pesquisar Pacientes")
        print(cabec)
        print("\n")
        cpf = input("Informe seu CPF:")
        paciente_encontrado = False
        for chave, valores in L1.items():
            if cpf in chave:
                paciente_encontrado = True
                print(valores)
                break  #Encerra o loop assim que encontrar o paciente
        if not paciente_encontrado:
            print('Paciente não Registrado!')
        FC.Save_Cadastro(L1)
        
        input("Digite Enter para voltar para o menu")
        os.system ('cls')
    elif opt == "3":  # Editar Dados
        print(cabec)
        print("\n")
        print("Alterar Cadastro")
        print(cabec)
        print("\n")
        cpf = input("Informe o CPF do paciente para editar os dados:")
        paciente_encontrado = False
        novos_dados = []
        for chave, valores in L1.items():
            if cpf in chave:
                paciente_encontrado = True
                print("Dados atuais do paciente:")
                print(valores)
                nome = input("Digite o novo nome: ")
                idade = input("Digite a nova data de nascimento: ")
                cartaoSus = input("Digite o novo cartão do SUS: ")
                cidade = input("Digite a nova cidade: ")
                novos_dados = [nome, idade, cartaoSus, cidade]
                L1[chave] = novos_dados
                print("Dados atualizados com sucesso!")
                break  # Encerra o loop assim que encontrar o paciente
        if paciente_encontrado:
            with open("dados.txt", 'r') as Dados:
                linhas = Dados.readlines()
            with open("dados.txt", 'w') as Dados:
                for linha in linhas:
                    if cpf in linha:
                        Dados.write(f"CPF: {cpf}, Nome: {novos_dados[0]}, Idade: {novos_dados[1]}, Cartão do Sus: {novos_dados[2]}, Cidade: {novos_dados[3]}\n")
                    else:
                        Dados.write(linha)
                FC.Save_Cadastro(L1)
        else:
            print('Paciente não Registrado!')
        os.system ('cls')
        input("Digite Enter para voltar para o menu")

    elif opt == "4":  # Excluir Paciente
        print(cabec)
        print("\n")
        print("Excluir Cadastro")
        print(cabec)
        print("\n")
        cpf = input("Informe o CPF do paciente para exclusão:")
        paciente_encontrado = False
        for chave, dados in L1.items():
            if cpf in chave:
                paciente_encontrado = True
                print("Dados do paciente encontrado:")
                print(dados)
                confirmacao = input("Tem certeza que deseja excluir este paciente? (S/N): ")
                if confirmacao.upper() == "S":
                    del L1[chave]
                    print("Paciente removido com sucesso!")
                    break  # Encerra o loop assim que encontrar o paciente

        if paciente_encontrado:
            with open("dados.txt", 'r') as Dados:
                linhas = Dados.readlines()
            with open("dados.txt", 'w') as Dados:
                for linha in linhas:
                    if cpf not in linha:
                        Dados.write(linha)
        else:
            print('Paciente não Registrado!')

        
        input("Digite Enter para voltar para o menu")

    elif opt == "5":  # Pesquisa Avançada de Paciente
        print ('''
________________________________________
Pesquisa Avançada
________________________________________
Escolha uma opção do Menu:
________________________________________
[1] Por CPF
[2] Por Nome
[3] Por Idade
[4] Pelo Cartão do Sus
[5] Pela Cidade
''')
        opcao = input("Escolha a opção do menu: ")
        os.system('cls')
        if opcao == "1":
            cpf = input("Informe o CPF para pesquisa: ")
            for chave, valores in L1.items():
                if cpf in chave:
                    paciente_encontrado = True
                    print(valores)
                    break  #Encerra o loop assim que encontrar o paciente
       
        elif opcao == "2":
            nome = input("Informe o nome para pesquisa: ")
            pacientes_encontrados = [valores for valores in L1.values() if nome.lower() == valores[0].lower()]
            if pacientes_encontrados:
                print("Pacientes encontrados com esse nome:")
                for paciente in pacientes_encontrados:
                    print(paciente)
            else:
                print('Nenhum paciente encontrado com esse nome!')
        elif opcao == "3":
            idade = input("Informe a idade para pesquisa: ")
            pacientes_encontrados = [valores for valores in L1.values() if idade == valores[1]]
            if pacientes_encontrados:
                print("Pacientes encontrados com essa idade:")
                for paciente in pacientes_encontrados:
                    print(paciente)
            else:
                print('Nenhum paciente encontrado com essa idade!')
        elif opcao == "4":
            cartao_sus = input("Informe o número do cartão do SUS para pesquisa: ")
            pacientes_encontrados = [valores for valores in L1.values() if cartao_sus == valores[2]]
            if pacientes_encontrados:
                for paciente in pacientes_encontrados:
                    print(paciente)
            else:
                print('Nenhum paciente encontrado com esse Cartão do SUS!')
        elif opcao == "5":
            cidade = input("Informe a cidade para pesquisa: ")
            pacientes_encontrados = [valores for valores in L1.values() if cidade.lower() in valores[3].lower()]

            if pacientes_encontrados:
                print("Pacientes encontrados nessa cidade:")
                for paciente in pacientes_encontrados:
                    print(paciente)
            else:
                print('Nenhum paciente encontrado nessa cidade!')
        input("Digite Enter para voltar para o menu")
        os.system('cls')

    elif opt == "6":
        print("Encerrando o programa e salvando dados...")
        FC.Save_Cadastro(L1)
        print("Dados salvos com sucesso!")
        break  # Encerra o loop e o programa


    #em desenvolvimento 
    # elif opt == "6":
    #    cidade_pesquisa = input("Informe a cidade para pesquisa:")
    #    pacientes_cidade = buscar_por_cidade(cidade_pesquisa, L1)
    #    
    #    if pacientes_cidade:
    #        print(f"Pacientes encontrados na cidade de {cidade_pesquisa}:")
    #        for paciente in pacientes_cidade:
    #           print(paciente)
    #    else:
    #        print(f"Nenhum paciente encontrado na cidade de {cidade_pesquisa}!")

    



