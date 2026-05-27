from modelagem.tests.database import engine
from sqlalchemy import text


try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))

        print("Conexao com o banco realizada com sucesso!")
        print("Tabelas encontradas:")

        for row in result:
            print("-", row[0])

except Exception as error:
    print("Erro ao conectar com o banco:")
    print(error)