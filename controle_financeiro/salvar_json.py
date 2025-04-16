import json
import os

def carregar_transacoes():

    #Caminho até o arquivo JSON onde vamos salvar os dados
    caminho_arquivo = os.path.join("dados","transacoes.json")

    os.makedirs("dados", exist_ok=True)


    #Verifica se o arquivo já existe
    if os.path.exists(caminho_arquivo):
        #Se existir, abrimos o arquivo no modo leitura
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            try:
                #Tentamos carregar os dados em formato JSON
                transacoes = json.load(arquivo)
                return transacoes
            except json.JSONDecodeError:
                #Se o arquivo estiver vazio ou mal formatado, retornamos uma lista vazia
                return []
    else:
        #Se o arquivo não existir, também retorna uma lista vazia
        return []

def salvar_transacoes(transacao):
    import json
    import os

    #definindo o caminho do arquivo
    caminho_arquivo = os.path.join("dados","transacoes.json")

    # Primeiro, tentamos carregar as transações existentes (usando a função que já criamos)
    transacoes_existentes = carregar_transacoes()

    # Adiciona a nova transação à lista
    transacoes_existentes.append(transacao)

    # Agora salvamos toda a lista atualizada no arquivo JSON
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(transacoes_existentes, arquivo, indent=4, ensure_ascii=False)