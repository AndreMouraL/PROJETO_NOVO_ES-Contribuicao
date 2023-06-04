from service import CadastroProduto
from produto_model import Produto
from service import ConsultaProduto

def test_produto():
    produto1 = Produto('IMPBROHL1','IMPRESSORA','BROTHER',1625.50,1)
    cadastroProduto= CadastroProduto()
    respostaCadastro= cadastroProduto.cadastrarProduto(produto1)
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