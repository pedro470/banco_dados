from contextlib import contextmanager
from typing import ContextManager
from contextManagerProprio import novaConexao
from mysql.connector.errors import ProgrammingError

sql = """
    INSERT INTO grupos (descricao) VALUES ("Os destemidos")
"""

with novaConexao() as conexao:
    try: 
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
    except ProgrammingError as p:
        print(f'O erro foi {p.msg}')
    else:
        print(f'{cursor.rowcount} novos registros foram adicionados')