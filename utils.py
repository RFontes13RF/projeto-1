import sqlite3
import os

def conecta_banco(nome_arquivo):
    conexao = sqlite3.connect(nome_arquivo)
    return conexao  

def load_data(nome_arquivo):
    conexao = conecta_banco(nome_arquivo)
    cursor = conexao.cursor()
    cursor.execute("SELECT title, content FROM note")
    dados = cursor.fetchall()
    conexao.close()
    return dados

def load_template(nome_arquivo):
    caminho = os.path.join('static', 'templates', nome_arquivo)

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return arquivo.read()

def cria_tabela(nome_arquivo):
    conexao = conecta_banco(nome_arquivo)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def add_anotacao(nome_arquivo, titulo, detalhes):
    conexao = conecta_banco(nome_arquivo)
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO note (title, content) VALUES (?, ?)",
        (titulo, detalhes)
    )
    conexao.commit()
    conexao.close()