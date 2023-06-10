from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    SKU = Column(String)
    nome = Column(String)
    fabricante = Column(String)
    valor = Column(Float)  

    def __init__(self, SKU, nome, fabricante, valor, id=None):
        self.id = id
        self.SKU = SKU
        self.nome = nome
        self.fabricante = fabricante
        self.valor = valor

    @property
    def valorProduto(self):
        return self.valor

    @property
    def get_codigo(self):
        return self.SKU

    @property
    def get_nomeProduto(self):
        return self.nome

    @property
    def get_nomeFabricante(self):
        return self.fabricante
    
    @property
    def get_id(self):
        return self.id