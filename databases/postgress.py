class PostgresDB:

    def __init__(self) -> None:
        self.__conexao = 'Postgress'

    def conectar(self) -> str:
        print('Conectando oa banco Postgress...')
        return self.__conexao
    
    def desconectar(self) -> str:
        print('Desconectando ao banco Postgres...')