from mysql.connector.errors import ProgrammingError
from contextManagerProprio import novaConexao

sql = "UPDATE contatos SET nome = 'Pedro' WHERE id = %s "
args = (3,)

with novaConexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as p:
        print(f'Erro na programação. A mensagem de erro é: {p.msg}')
    else:
        print(f'{cursor.rowcount} registros deletados')
    
