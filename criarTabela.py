from contextManagerProprio import novaConexao
from mysql.connector import ProgrammingError

tabelaContatos = """
    CREATE TABLE IF NOT EXISTS contatos
        (nome VARCHAR(50), tel VARCHAR(40))
"""

tabelaEmails = """
    CREATE TABLE IF NOT EXISTS emails
        (id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50))
"""

with novaConexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabelaContatos)
        cursor.execute(tabelaEmails)
    except ProgrammingError as e:
        print('Erro: ',e.msg)  