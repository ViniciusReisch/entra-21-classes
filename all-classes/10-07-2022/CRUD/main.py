import sqlite3

conexao = sqlite3.connect('meu primeiro banco.db')
cursor = conexao.cursor()

cursor.execute('DROP TABLE frutas')
conexao.commit()
# # CRUD
# # Create
#
# cursor.execute('CREATE TABLE IF NOT EXISTS frutas ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'tipo TEXT)')
# conexao.commit()
#
# # cursor.execute('INSERT INTO frutas(nome, tipo)'
# #                'VALUES("maça", "verde")')
# # conexao.commit()
#
# # Update
#
# cursor.execute('UPDATE frutas SET nome="banana" WHERE id=1')
# conexao.commit()
#
# # Jamais faras UPDATE sem WHERE
#
# # Read
#
# cursor.execute('SELECT * FROM frutas WHERE nome="banana"')
# for linha in cursor.fetchall():
#     print(f'{linha[0]} - {linha[1]} - {linha[2]}')
# print("="*23)
# cursor.execute('DELETE FROM frutas WHERE id=2')
# conexao.commit()
#
# cursor.execute('SELECT * FROM frutas')
# for linha in cursor.fetchall():
#     print(f'{linha[0]} - {linha[1]} - {linha[2]}')

cursor.close()
conexao.close()

