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

            


