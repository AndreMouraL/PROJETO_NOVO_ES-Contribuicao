from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    codigo = Column(String)
    nomeProduto = Column(String)
    nomeFabricante = Column(String)
    _valorProduto = Column(Float)  

    def __init__(self, codigo, nomeProduto, nomeFabricante, valorProduto, id=None):
        self.id = id
        self.codigo = codigo
        self.nomeProduto = nomeProduto
        self.nomeFabricante = nomeFabricante
        self._valorProduto = valorProduto

    @property
    def valorProduto(self):
        return self._valorProduto

    @property
    def codigo(self):
        return self.codigo

    @property
    def nomeProduto(self):
        return self.nomeProduto

    @property
    def nomeFabricante(self):
        return self.nomeFabricante
    
    @property
    def id(self):
        return self.id