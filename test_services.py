from produto_model import Produto
from service import *
from estoque import Estoque

estoque = Estoque()

def test_cadastro_produtos():
    produto1 = Produto('IMPBROHL1','IMPRESSORA','BROTHER',1625.50,1)
    cadastroProduto= CadastroProduto(estoque.estoque)
    respostaCadastro= cadastroProduto.cadastrarProduto(produto1)
    assert "Cadastrado com Sucesso!" == respostaCadastro


def test_consulta_produtos():
    produtos_estoque = estoque.estoque
    consultaProduto = ConsultaProduto(produtos_estoque) 
    respostaConsulta = consultaProduto.consultarProduto(1)
    assert 'produto_model.Produto object at' in str(respostaConsulta)

   
def test_lista_produtos():
    listar_estoque = estoque.estoque
    listaProdutos =  ListaProdutos(listar_estoque)
    respostaListar = listaProdutos.listarProdutos()
    assert "Todos os produtos foram encontrados!" == respostaListar


def test_atualiza_produtos():
    produtos_estoque = estoque.estoque
    atualizaProduto = AtualizaProduto(produtos_estoque,1)
    respostaAtualizar = atualizaProduto.atualizarProduto('IMPEPSO641', 'IMPRESSORA', 'EPSON', 2650.55)
    assert "Produto atualizado com Sucesso!" == respostaAtualizar


def test_deleta_produtos():
    produtos_estoque = estoque.estoque  
    deletaProduto  =  DeletaProduto(produtos_estoque)
    respostaDeletar = deletaProduto.deletarProduto(1)
    assert "Produto deletado com Sucesso!" ==  respostaDeletar


test_cadastro_produtos()
test_consulta_produtos()
test_lista_produtos()
test_atualiza_produtos()
test_deleta_produtos()
