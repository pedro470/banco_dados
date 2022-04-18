from mysql.connector.errors import ProgrammingError
from contextManagerProprio import novaConexao

sql = "SELECT id FROM grupos WHERE descricao = %s"
sql2 = "UPDATE contatos SET grupo_id = %s WHERE nome = %s"

args = {
    "Pedro": "Os destemidos"
}

with novaConexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in args.items():
            cursor.execute(sql, (grupo,))
            identidade = cursor.fetchone()[0]
            cursor.execute(sql2, (identidade,contato))
            conexao.commit()
    except ProgrammingError as p:
        print(f'A mensagem de erro foi: {p.msg}')