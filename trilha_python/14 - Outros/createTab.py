# script para inserir dados do login
import sqlite3
import hashlib
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()
vnome = input('Digite o nome para o login: ')
vsenha = input('Digite uma senha para o login: ')
d = hashlib.md5()
d.update(vsenha.encode('utf-8'))
cursor.execute('insert into usuario values ("%s", "%s")' % (vnome, d))
conn.commit()
print("senha hash gerada: ",d.hexdigest())
input("Pressione ENTER para sair...")