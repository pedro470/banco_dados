from typing import final
from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from contextlib import contextmanager

parametros = dict(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '12345678',
    database = 'agenda'
)

@contextmanager
def novaConexao():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if conexao and (conexao.is_connected()):
            conexao.close()