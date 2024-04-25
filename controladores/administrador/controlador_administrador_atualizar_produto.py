from flask import request, make_response, jsonify

from bancodedados.modelos.Produtos import Produtos
from bancodedados.modelos.Usuarios import Usuarios

def administrador_atualizar_produto (usuario_id) :
    req = request.get_json()
    produto_encontrado = None

    usuario_encontrado = Usuarios.get_by_id(usuario_id)
    if not usuario_encontrado :
        return make_response(
            jsonify("Usuário não encontrado"),
            404
        )
    
    produto_encontrado = Produtos.get_by_id(req['produto_id'])
    produto_encontrado.descricao = req['descricao']
    produto_encontrado.valor = req['valor']
    produto_encontrado.categoria_id = req['categoria_id']
    produto_encontrado.audio = req['audio']
    produto_encontrado.imagem = req['imagem']
    produto_encontrado.video = req['video']
    produto_encontrado.save()

    return make_response(
        jsonify("Produto atualizado"),
        201
    )
    