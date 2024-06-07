from flask import request, make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Produtos import Produtos
from bancodedados.modelos.Usuarios import Usuarios

def administrador_deletar_produto() :

    req = request.get_json()
    usuario = get_jwt_identity()

    try :

        usuario_encontrado = Usuarios.select().where(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário inálido!"),
                404
            )
        
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
    
    except ArithmeticError :
        return NameError