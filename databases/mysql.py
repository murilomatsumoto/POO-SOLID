class Mysql:

    def __init__(self) -> None:
        self.__conexao = 'Mysql'

    def conectar(self) -> str:
        print('Conectando oa banco mysql...')
        return self.__conexao
    
    def desconectar(self) -> str:
        print('Desconectando ao banco mysql...')