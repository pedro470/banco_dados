from mysql.connector import connect

conexao = connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '12345678'
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE agenda')