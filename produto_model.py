class Produto:
    def __init__(self, codigo, nomeProduto, nomeFabricante, valorProduto, id=None):
        self.ID = id
        self.SKU = codigo
        self.nome = nomeProduto
        self.fabricante = nomeFabricante
        self.valor = valorProduto