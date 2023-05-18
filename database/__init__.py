from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine('sqlite:///database/database.db') #faz a conexão com o banco
Session = sessionmaker(bind=engine) #Cria-se a sessão
session = Session()

class Base(DeclarativeBase): #irá conter todos os metadados da conexão com o banco de dados
    pass

Base.metadata.create_all(engine)



    



