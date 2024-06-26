from flask import request, make_response, jsonify
from bancodedados.modelos.Produtos import Produtos
from bancodedados.modelos.Usuarios import Usuarios

def administrador_deletar_produto(usuario_id) :
    usuario_encontrado = Usuarios.get_by_id(usuario_id)
    if not usuario_encontrado :
        return make_response(
            jsonify("Usuário inálido!"),
            404
        )
    
    req = request.get_json()
    produto_encontrado = Produtos.get_by_id(req['produto_id'])
    if not produto_encontrado :
        return make_response(
            jsonify("Produto não encontrado!")
        )
    
    produto_deletado = Produtos.delete_by_id(req['produto_id'])
    if not produto_deletado :
        return make_response(
            jsonify("Erro interno do servidor"),
            500
        )
    
    return (make_response(
        jsonify("Produto deletado com sucesso"),
        204
    ))