from contextManagerProprio import novaConexao

with novaConexao() as conexao:
    if conexao.is_connected():
        print('conectado!')

