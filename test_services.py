from service import CadastroProduto
from produto_model import Produto
from service import ConsultaProduto
from service import ListaProdutos
from service import AtualizaProduto


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
    respostaConsulta = consultaProduto.consultarProduto(1)
    assert 'produto_model.Produto object at' in str(respostaConsulta)

    listar_estoque = cadastroProduto.produtosCadastrados
    listaProdutos =  ListaProdutos(listar_estoque)
    respostaListar = listaProdutos.listarProdutos()
    assert "Todos os produtos foram encontrado!" == respostaListar

    produtos_estoque = cadastroProduto.produtosCadastrados
    atualizaProduto = AtualizaProduto(produtos_estoque,1)
    respostaAtualizar = atualizaProduto.atualizarProduto('IMPEPSO641', 'IMPRESSORA', 'EPSON', 2650.55)
    assert "Produto atualizado com Sucesso!" == respostaAtualizar

    listar_estoque = cadastroProduto.produtosCadastrados
    listaProdutos =  ListaProdutos(listar_estoque)
    respostaListar = listaProdutos.listarProdutos()
    assert "Todos os produtos foram encontrado!" == respostaListar
    
    deletaProduto  =  DeletaProduto(produtos_estoque)
    respostaDeletar = deletaProduto.deletarProduto(3)
    assert "Produto deletado com Sucesso!" ==  respostaDeletar
test_produto()