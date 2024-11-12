from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base()

class Usuario(Base):
    # Definindo caracteristicas da tabela
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)


    # Definindo atributos da classe
    def __init__(self, nome: str, email: str, idade: str) -> None:  
        self.nome = nome
        self.email = email
        self.idade = idade

    def to_dict(self):
        """Converte o objeto Usuario para um dicionário."""
        return {
            'Id': self.id,
            'Nome': self.nome,
            'Email': self.email,
            'Idade': self.idade
        }

# Criando tabelas na db.
Base.metadata.create_all(bind=db)