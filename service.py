class CadastroProduto:
    def __init__(self):
        self.produtosCadastrados = []
    def cadastrarProduto(self, produto):
        self.produtosCadastrados.append(produto)
        if len(self.produtosCadastrados) > 0:
            return "Cadastrado com Sucesso!"

class ConsultaProduto:
    def __init__(self, estoque):
        self.produtosCadastrados = estoque
    def consultarProduto (self, id_produto):
        for produto in self.produtosCadastrados:
            if produto.ID == id_produto:
                return "Produto encontrado com Sucesso!"


class ListaProdutos:
    def __init__(self, estoque):
        self.produtosCadastrados = estoque
        self.listaEstoque = []
    def listarProdutos (self):
        Produto = []
        for produto in self.produtosCadastrados:
            Produto.append(produto.ID)
            Produto.append(produto.SKU)
            Produto.append(produto.nome)
            Produto.append(produto.fabricante)
            Produto.append(produto.valor)
            self.listaEstoque.append(Produto.copy())
            Produto = []
        if len(self.produtosCadastrados) == len(self.listaEstoque):
            return "Todos os produtos foram encontrado!"
