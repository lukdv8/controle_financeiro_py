import sqlite3 as lite

con = lite.connect('dados.db')

# funções para inserir

def inserirCategoria(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome) VALUES (?)"
        cur.execute(query, i)

def inserirReceita(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receita (Categoria, adicionado_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, i)

def inserirGasto(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Despesa (Categoria, gasto_em, valor) VALUES (?, ?, ?)"
        cur.execute(query, i)

# funções para deletar

def deletarReceita(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receita WHERE id=?"
        cur.execute(query, i)

def deletarDespesa(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Despesa WHERE id=?"
        cur.execute(query, i)

'''
# Listar todas as tabelas
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()
print(tabelas)  # Verifique se "Categoria" aparece na lista
'''

'''
# Executar uma consulta para acessar todos os registros da tabela 'Categoria'
cursor = con.cursor()
cursor.execute("SELECT * FROM Categoria")

# Recuperar todos os resultados da consulta
categorias = cursor.fetchall()

# Iterar e exibir os resultados
for categoria in categorias:
    print(f"ID: {categoria[0]}, Nome: {categoria[1]}")
'''

'''
# Apagar um registro específico da tabela 'Categoria' pelo 'id'
cursor = con.cursor()

id_categoria = 3  # Exemplo: queremos apagar a categoria com id 1

cursor.execute("DELETE FROM Categoria WHERE id = ?", (id_categoria,))

# Confirmar a transação (salvar as alterações no banco de dados)
con.commit()

print(f"Categoria com id {id_categoria} apagada.")

# Fechar o cursor e a conexão
cursor.close()
con.close()
'''