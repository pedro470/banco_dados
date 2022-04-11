from mysql.connector.errors import ProgrammingError
from contextManagerProprio import novaConexao

sql = 'SELECT * FROM CONTATOS'

with novaConexao() as conexao:
    try:    
        cursor = conexao.cursor()   
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as p:
        print(f'Você errou na programação. O erro foi: {p.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]} - {contato[0]} \t telefone: {contato [1]}')
