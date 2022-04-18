from contextManagerProprio import novaConexao
from mysql.connector.errors import ProgrammingError

sql = """
    SELECT
        grupos.descricao AS grupo,
        contatos.nome AS contato
    FROM contatos
    INNER JOIN grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, contato

"""

with novaConexao() as conexao:
    try:
        try:
            cursor = conexao.cursor(dictionary = True)
            cursor.execute(sql)
            resultado = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as p:
        print(f'A mensagem de erro é: {p.msg}')
    else:
        for contato in resultado:
            print(f'Contato: {contato["contato"]},  Grupo: {contato["grupo"]}')