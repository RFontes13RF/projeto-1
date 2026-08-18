import json
import os

def load_data(nome_arquivo):
    caminho = os.path.join("static", "data", nome_arquivo)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def load_template(nome_arquivo):
    caminho = os.path.join('static', 'templates', nome_arquivo)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def add_anotacao(nome_arquivo, nova_anotacao):
    caminho = os.path.join("static", "data", nome_arquivo)
    dados = load_data(nome_arquivo)
    dados.append(nova_anotacao)
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo)