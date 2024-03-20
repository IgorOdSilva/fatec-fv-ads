# Carrega Txt
def Load_Txt():
    L1 = {}  # Dicionário que receberá os dados
    try:
        with open("dados.txt", 'r') as Dados:
            for line in Dados:
                elements = line.rstrip().split(",")
                if len(elements) == 5:  # Verifica se há exatamente 5 elementos em cada linha
                    L1[elements[0]] = [elements[1], elements[2], elements[3], elements[4]]
                else:
                    print("")
                    return {}  # Retorna um dicionário vazio se o formato estiver incorreto
        return L1
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return {}  # Retorna um dicionário vazio se o arquivo não for encontrado

def Save_Cadastro(dados):
    try:
        with open("dados.txt", 'w') as Dados:
            Dados.write("Dados do Paciente\n")  # Escreve o cabeçalho apenas uma vez

        with open("dados.txt", 'a') as Dados:
            for chave, valores in dados.items():
                if len(valores) == 4:  # Verifica se há exatamente 4 elementos para cada valor do dicionário
                    linha = f"CPF: {chave}, Nome: {valores[0]}, Idade: {valores[1]}, Cartão do Sus: {valores[2]}, Cidade: {valores[3]}\n"
                    Dados.writelines(linha)
                else:
                    print(f"Erro: Dados inválidos para gravação na chave '{chave}'.")
        return True
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        return False

def buscar_por_cidade(cidade, dados):
    pacientes_encontrados = []
    for chave, info in dados.items():
        if info[3].lower() == cidade.lower():
            pacientes_encontrados.append(info)
    return pacientes_encontrados




 