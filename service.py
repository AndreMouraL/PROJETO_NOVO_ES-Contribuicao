class CadastroProduto:
    def __init__(self):
        self.produtosCadastrados = []
    def cadastrarProduto(self, produto):
        self.produtosCadastrados.append(produto)
        if len(self.produtosCadastrados) > 0:
            return "Cadastrado com Sucesso!"