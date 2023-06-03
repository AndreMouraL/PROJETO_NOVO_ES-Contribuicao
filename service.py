class CadastroProduto:
    def __init__(self):
        self.produtosCadastrados = []
    def cadastrarProduto(self, produto):
        self.produtosCadastrados.append(produto)
        return "Cadastrado com Sucesso!"