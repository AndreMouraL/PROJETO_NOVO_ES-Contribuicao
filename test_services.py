from produto_model import Produto
from service import *

def test_cadastro_produtos():
    produto1 = Produto('IMPBROHL1', 'IMPRESSORA', 'BROTHER', 1625.50)
    cadastroProduto = CadastroProduto()
    respostaCadastro = cadastroProduto.cadastrarProduto(produto1)
    assert "Cadastrado com Sucesso!" == respostaCadastro


def test_consulta_produtos():
    consultaProduto = ConsultaProduto() 
    respostaConsulta = consultaProduto.consultarProduto(1)
    assert 'Operação realizada com Sucesso!' == respostaConsulta[1]

   
def test_lista_produtos():
    listaProdutos =  ListaProdutos()
    respostaListar = listaProdutos.listarProdutos()
    assert "Todos os produtos foram encontrados!" == respostaListar


def test_atualiza_produtos():
    atualizaProduto = AtualizaProduto(1)
    respostaAtualizar = atualizaProduto.atualizarProduto('IMPEPSO641', 'IMPRESSORA', 'EPSON', 2650.55)
    assert "Produto atualizado com Sucesso!" == respostaAtualizar


def test_deleta_produtos():
    deletaProduto  =  DeletaProduto()
    respostaDeletar = deletaProduto.deletarProduto(1)
    assert "Produto deletado com Sucesso!" ==  respostaDeletar


# test_cadastro_produtos()
# test_consulta_produtos()
# test_lista_produtos()
# test_atualiza_produtos()
# test_deleta_produtos()
