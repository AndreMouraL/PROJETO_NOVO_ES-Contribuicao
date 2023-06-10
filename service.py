from produto_model import Produto
from conexão import ConexaoBancoDados



class CadastroProduto:
    def __init__(self):
        self.conn = ConexaoBancoDados()
    def cadastrarProduto(self, produto):
        self.conn.session.add(produto)
        self.conn.session.commit()
        mensagem = self.conn.fecharConexao()
        if mensagem  == "Operação realizada com Sucesso!":
            return "Cadastrado com Sucesso!"




class ConsultaProduto:
    def __init__(self):
        self.conn = ConexaoBancoDados()
    def consultarProduto (self, id_produto):
        produto = self.conn.session.query(Produto).get(id_produto)
        mensagem = self.conn.fecharConexao() 
        return produto, mensagem



class ListaProdutos:
    def __init__(self):
        self.conn = ConexaoBancoDados()
    def listarProdutos (self):
        produtos = self.conn.session.query(Produto).all()
        if produtos:
            for produto in produtos:
                print("ID:", produto.id)
                print("Código:", produto.codigo)
                print("Nome do Produto:", produto.nomeProduto)
                print("Nome do Fabricante:", produto.nomeFabricante)
                print("Valor do Produto:", produto.valorProduto)
                mensagem = self.conn.fecharConexao()
                if mensagem  == "Operação realizada com Sucesso!":
                    return "Todos os produtos foram encontrados!"
        else:
            print("Não existem produtos cadastrados.")




class AtualizaProduto:
    def __init__(self, id):
        self.conn = ConexaoBancoDados()
        self.produto_p_alterar = self.conn.session.query(Produto).get(id)
    def atualizarProduto(self, sku, nome, fabricante, valor):
        if self.produto_p_alterar is not None:
            self.produto_p_alterar.codigo = sku
            self.produto_p_alterar.nomeProduto = nome
            self.produto_p_alterar.nomeFabricante = fabricante
            self.produto_p_alterar.valorProduto = valor
            self.conn.session.merge(self.produto_p_alterar)
            self.conn.session.commit()
            mensagem = self.conn.fecharConexao()
            if mensagem  == "Operação realizada com Sucesso!":
                print("Produto atualizado com sucesso!")
                return "Produto atualizado com sucesso!"
        else:
            print("Produto não encontrado.")



class DeletaProduto:
    def __init__(self):
        self.conn = ConexaoBancoDados()
    def deletarProduto(self, id):
        produto_p_deletar = self.conn.session.query(Produto).get(id)
        if produto_p_deletar is not None:
            self.conn.session.delete(produto_p_deletar)
            self.conn.session.commit()
            mensagem = self.conn.fecharConexao()
            if mensagem  == "Operação realizada com Sucesso!":
                print("Produto deletado com sucesso.")
                return "Produto deletado com Sucesso!"
        else:
            print("Produto não encontrado.")



    '''
    verificando consulta:
    print(f'id: {produto.getID()}\nSKU: {produto.getSKU()}\nNome: {produto.getNome()}\n
    Marca: {produto.getFabricante()}\nValor: {produto.getValor()}\n')
    
    verificando lista:
    print(self.listaEstoque)
    '''