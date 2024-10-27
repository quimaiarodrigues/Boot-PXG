import sqlite3  # Biblioteca para trabalhar com SQLite
import ast  # Necessário para converter a string do banco para lista Python


def carregar_rota(nome_rota):
    conexao = sqlite3.connect('rotas.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT movimentos FROM rotas WHERE nome = ?', (nome_rota,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        # Converte para lista de movimentos
        movimentos = ast.literal_eval(resultado[0])
        return movimentos
    return None


# Função para inicializar o banco de dados e criar a tabela


def inicializar_banco_dados():
    conexao = sqlite3.connect('rotas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            movimentos TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()

# Função para salvar uma nova rota


def salvar_rota(nome_rota, movimentos):
    conexao = sqlite3.connect('rotas.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO rotas (nome, movimentos) VALUES (?, ?)',
                   (nome_rota, str(movimentos)))
    conexao.commit()
    conexao.close()

# Função para excluir uma rota pelo nome


def excluir_rota(nome_rota):
    conexao = sqlite3.connect('rotas.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM rotas WHERE nome = ?', (nome_rota,))
    conexao.commit()
    conexao.close()

# Função para listar todas as rotas


def listar_rotas():
    conexao = sqlite3.connect('rotas.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT nome, movimentos FROM rotas')
    rotas = cursor.fetchall()
    conexao.close()
    return rotas


# Inicializar banco de dados ao iniciar
inicializar_banco_dados()
