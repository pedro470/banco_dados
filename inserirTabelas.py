from mysql.connector.errors import ProgrammingError
from contextManagerProprio import novaConexao

query = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('DROP TABLE emails', '98765-4321')

with novaConexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(query, args)
        conexao.commit()
    except ProgrammingError as e:
        print('Erro: ',e.msg)
    