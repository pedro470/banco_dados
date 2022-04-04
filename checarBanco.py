from mysql.connector import connect

conexao = connect(
    user = 'root',
    host = 'localhost',
    password = '12345678',
    port = 3306
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')
print(enumerate(cursor, start=1))

for i, database in enumerate(cursor, start=1):
    print(f'Banco de dados {i}: {database[0]}')