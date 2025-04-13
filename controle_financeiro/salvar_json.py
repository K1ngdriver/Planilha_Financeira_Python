import json
import os

def carregar_transacoes():

    #Caminho até o arquivo JSON onde vamos salvar os dados
    caminho_arquivo = os.path.json("dados","transacoes.json")

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