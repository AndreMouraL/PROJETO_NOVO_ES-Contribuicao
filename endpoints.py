from fastapi import FastAPI
from produto_model import Produto
from service import *
from pydantic import BaseModel

app = FastAPI()

class ProdutoModel(BaseModel):
    id: int
    SKU: str
    nome: str
    fabricante: str
    valor: float

# Instanciando as classes de serviço
cadastro_produto = CadastroProduto()
consulta_produto = ConsultaProduto()
lista_produtos = ListaProdutos()
atualiza_produto = AtualizaProduto(1)  # Insira o ID do produto a ser atualizado
deleta_produto = DeletaProduto()

# Rotas
@app.post("/produto/cadastrar", response_model=ProdutoModel)
def cadastrar_produto(produto: ProdutoModel):
    return cadastro_produto.cadastrarProduto(Produto(
        id=produto.id,
        SKU=produto.SKU,
        nome=produto.nome,
        fabricante=produto.fabricante,
        valor=produto.valor
    ))

@app.get("/produto/consultar/{id_produto}")
def consultar_produto(id_produto: int):
    return consulta_produto.consultarProduto(id_produto)

@app.get("/produto/listar")
def listar_produtos():
    return lista_produtos.listarProdutos()

@app.put("/produto/atualizar/{id_produto}")
def atualizar_produto(produto: ProdutoModel):
    return atualiza_produto.atualizarProduto(produto.SKU, produto.nome, produto.fabricante, produto.valor)

@app.delete("/produto/deletar/{id_produto}")
def deletar_produto(id_produto: int):
    return deleta_produto.deletarProduto(id_produto)