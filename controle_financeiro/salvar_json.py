import json
import os
from datetime import datetime

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

    #definindo o caminho do arquivo
    caminho_arquivo = os.path.join("dados","transacoes.json")

    # Primeiro, tentamos carregar as transações existentes (usando a função que já criamos)
    transacoes_existentes = carregar_transacoes()

    # Adiciona a nova transação à lista
    transacoes_existentes.append(transacao)

    # Agora salvamos toda a lista atualizada no arquivo JSON
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(transacoes_existentes, arquivo, indent=4, ensure_ascii=False)

def mes_atual():
    caminho_arquivo = os.path.join("dados", "transacoes.json")

    if not os.path.join(caminho_arquivo):
        print("Nenhum dado existente.")
        return[]
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        try:
            transacoes = json.load(arquivo)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo JSON.")
            return []
        
    hoje = datetime.today()
    ano_atual = hoje.year()
    mes_atual = hoje.month()

    transacoes_filtradas = []

    for transacao in transacoes:
        try:
            data = datetime.strptime(transacao["data"], "%Y-%m-%d")
            if data.year == ano_atual and data.month == mes_atual:
                transacoes_filtradas.append(transacao)
        except Exception as e:
            print(f"Erro ao processar transação: {e}")
    return transacoes_filtradas