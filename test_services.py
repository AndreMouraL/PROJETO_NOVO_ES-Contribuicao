from service import CadastroProduto
from produto_model import Produto

def test_cadastro_produto():
    produto = Produto('IMPBROHL1','IMPRESSORA','BROTHER',1625.50)
    cadastroProduto= CadastroProduto()
    resposta = cadastroProduto.cadastrarProduto(produto)
    assert "Cadastrado com Sucesso!" == resposta


test_cadastro_produto()