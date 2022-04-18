from contextManagerProprio import novaConexao
from mysql.connector import ProgrammingError

tabelaGrupo = """
    CREATE TABLE IF NOT EXISTS grupos
    (id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(30))
"""

alterarContato1 = """
    ALTER TABLE contatos ADD grupo_id INT

"""

alterarContato2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id)
    REFERENCES  grupos(id)

"""

with novaConexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabelaGrupo)
        cursor.execute(alterarContato1)
        cursor.execute(alterarContato2)
    except ProgrammingError as e:
        print('Erro: ',e.msg)  