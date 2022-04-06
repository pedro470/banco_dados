from contextManagerProprio import novaConexao

with novaConexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute('SHOW TABLES')

for i, tabela in enumerate(cursor,start=1):
    print(f'Tabela {i}: {tabela[0]}')