from service import CadastroProduto
from produto_model import Produto
from service import ConsultaProduto
from service import ListaProdutos

def test_produto():
    produto1 = Produto('IMPBROHL1','IMPRESSORA','BROTHER',1625.50,1)
    produto2 = Produto('IMPBROHL2','IMPRESSORA','BROTHER',1625.50,2)
    produto3 = Produto('IMPBROHL3','IMPRESSORA','BROTHER',1625.50,3)
    produto4 = Produto('IMPBROHL4','IMPRESSORA','BROTHER',1625.50,4)
    cadastroProduto= CadastroProduto()
    respostaCadastro= cadastroProduto.cadastrarProduto(produto1)
    respostaCadastro= cadastroProduto.cadastrarProduto(produto2)
    respostaCadastro= cadastroProduto.cadastrarProduto(produto3)
    respostaCadastro= cadastroProduto.cadastrarProduto(produto4)
    assert "Cadastrado com Sucesso!" == respostaCadastro

    produtos_estoque = cadastroProduto.produtosCadastrados
    consultaProduto = ConsultaProduto(produtos_estoque) 
    respostaConsulta= consultaProduto.consultarProduto(1)
    assert "Produto encontrado com Sucesso!" == respostaConsulta

    listar_estoque = cadastroProduto.produtosCadastrados
    listaProdutos =  ListaProdutos(listar_estoque)
    respostaListar = listaProdutos.listarProdutos()
    assert "Todos os produtos foram encontrado!" == respostaListar
    
test_produto()