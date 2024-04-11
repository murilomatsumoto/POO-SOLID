from repositorio import Repositorio
from databases import PostgresDB, Mysql

db_conn_posgress= PostgresDB()
db_conn_mysql= Mysql()
repo = Repositorio()

repo.insert(db_conn_posgress)
print()
repo.insert(db_conn_mysql)