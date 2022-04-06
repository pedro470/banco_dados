from mysql.connector.errors import ProgrammingError
from contextManagerProprio import novaConexao

sql = 'ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

with novaConexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as p:
        print(f"Você programou errado. Seu erro foi:\n {p.msg}")
