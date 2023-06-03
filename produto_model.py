class Produto:
    def __init__(self, codigo, nomeProduto, nomeFabricante, valorProduto, id=None):
        self.ID = id
        self.SKU = codigo
        self.nome = nomeProduto
        self.fabricante = nomeFabricante
        self.valor = valorProduto

    def getID(self):
        return self.ID
    
    def getSKU(self):
        return self.SKU

    def getNome(self):
        return self.nome

    def getFabricante(self):
        return self.fabricante

    def getValor(self):
        return self.valor
