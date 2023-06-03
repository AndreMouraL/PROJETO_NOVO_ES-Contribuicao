def test_cadastro_produto():
    produto = Produto()
    cadastroProduto= CadastroProduto()
    resposta = CadastrarProduto(produto)
    assert "Cadastrado com Sucesso!" == resposta


test_cadastro_produto()