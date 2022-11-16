#1°passo - Importar biblioteca sqlite3
import sqlite3

#2°passo - Estabelecer conexão com o banco de dados
conexao = sqlite3.connect("dc_universe.db")

#3°passo - Criar o cursor  
cursor = conexao.cursor()

#4°passo - Comando SQL do Banco
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#5°passo - Execução do comando no banco (SQL no SQLITE - no cursor)
cursor.execute(sql)

#6°passo - Exibir a consulta com os dados da base
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

for pessoa in pessoas:
  print(f"Nome: {pessoa[1]} ({pessoa[3]})")