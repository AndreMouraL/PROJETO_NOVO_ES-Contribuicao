from produto_model import Produto
from estoque import Estoque


class CadastroProduto:
    def __init__(self, estoque):
        self.produtosCadastrados = []
        self.estoque =  estoque
    def cadastrarProduto(self, produto):
        self.produtosCadastrados.append(produto)
        if len(self.produtosCadastrados) > 0:
            self.estoque.append(produto)
            self.produtosCadastrados = []
            return "Cadastrado com Sucesso!"

class ConsultaProduto:
    def __init__(self, estoque):
        self.produtosCadastrados = estoque
    def consultarProduto (self, id_produto):
        for produto in self.produtosCadastrados:
            if produto.getID() == id_produto:
                return produto


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
            return "Todos os produtos foram encontrados!"


class AtualizaProduto:
    def __init__(self, estoque, id):
        self.produtosCadastrados = estoque
        self.idaltera = id
    def atualizarProduto (self, sku, nome, fabricante, valor):
        consultaProduto = ConsultaProduto(self.produtosCadastrados)
        ProdutoAtualizando = consultaProduto.consultarProduto(self.idaltera)
        indice = self.produtosCadastrados.index(ProdutoAtualizando)
        ProdutoAtualizando.setSKU(sku)
        ProdutoAtualizando.setNome(nome)
        ProdutoAtualizando.setFabricante(fabricante)
        ProdutoAtualizando.setValor(valor)
        self.produtosCadastrados[indice] = ProdutoAtualizando
        atualizaEstoque = Estoque()
        atualizaEstoque.estoque == self.produtosCadastrados
        return "Produto atualizado com Sucesso!"
    
class DeletaProduto:
    def __init__(self, estoque):
        self.produtosCadastrados = estoque
    def deletarProduto(self, id):
        consultaProduto = ConsultaProduto(self.produtosCadastrados)
        Produtodeletando = consultaProduto.consultarProduto(id)
        indice = self.produtosCadastrados.index(Produtodeletando)
        del self.produtosCadastrados[indice]
        atualizaEstoque = Estoque()
        atualizaEstoque.estoque == self.produtosCadastrados
        return "Produto deletado com Sucesso!"
    
















    '''
    verificando consulta:
    print(f'id: {produto.getID()}\nSKU: {produto.getSKU()}\nNome: {produto.getNome()}\n
    Marca: {produto.getFabricante()}\nValor: {produto.getValor()}\n')
    
    verificando lista:
    print(self.listaEstoque)
    '''