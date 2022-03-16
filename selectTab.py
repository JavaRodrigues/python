# script para listar os logins dos usuários
import sqlite3
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM usuario;' )
for i in cursor.fetchall():
       print(i)
input('Pressione ENTER para sair...')
