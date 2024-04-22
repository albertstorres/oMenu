from flask import request, make_response, jsonify
from bancodedados.modelos.Categorias import Categorias
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Produtos import Produtos


def administrador_cadastrar_produto (usuario_id) :
    req = request.get_json()

    administrador_encontrado = Usuarios.get_by_id(usuario_id)
    print(administrador_encontrado)
    if not administrador_encontrado :
        return "Administrador não cadastrado!"
    
    categoria_encontrada = Categorias.get_by_id(req['categoria_id'])
    if not categoria_encontrada :
        return "Categoria não cadastrada!"
    
    produto_cadastrado = Produtos.create(
        descricao = req['descricao'],
        valor = req['valor'] * 100, 
        categoria_id = req['categoria_id'],
        audio = req['audio'],
        imagem = req['imagem'],
        video = req['video'],
    )
    if not produto_cadastrado :
        return "Erro interno do servidor!"
    
    return "Produto cadastrado com sucesso!"
