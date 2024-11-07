# importando SQLite
import sqlite3 as lite

# criando conexao
con = lite.connect('dados.db')

# cria a tabela de categoria
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Categoria (Id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

# cria a tabela de receita
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Receita (Id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, adicionado_em DATE, valor DECIMAL)")

# cria a tabela de despesas
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Despesa (Id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, gasto_em DATE, valor DECIMAL)")