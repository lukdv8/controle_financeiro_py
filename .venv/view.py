import sqlite3 as lite

con = lite.connect('dados.db')

# funções para inserir

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receita (Categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, i)

def inserir_gasto(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Despesa (Categoria, gasto_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, i)

# funções para deletar

def deletar_receita(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receita WHERE id=?"
        cur.execute(query, i)

def deletar_despesa(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Despesa WHERE id=?"
        cur.execute(query, i)

# funções para ver dados

def ver_categoria():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

def ver_receitas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receitas")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

def ver_despesas():
    lista_itens = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Despesa")
        linha = cur.fetchall()
        for l in linha:
            lista_itens.append(l)

    return lista_itens

print(ver_despesas())