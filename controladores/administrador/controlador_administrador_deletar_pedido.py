from flask import make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Pedidos import Pedidos
from bancodedados.modelos.Usuarios import Usuarios

def administrador_deletar_pedido (pedido_id) :
    usuario = get_jwt_identity()

    try :

        usuario_encontrado = Usuarios.select().where(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário não cadastrado"),
                404
            )
        
        pedido_encontrado = Pedidos.select().where(Pedidos.id == pedido_id).dicts()
        if not pedido_encontrado :
            return make_response(
                jsonify("Pedido não cadastrado."),
                404
            )
        
        pedido_deletado = Pedidos.delete_by_id(pedido_id)
        if not pedido_deletado :
            return make_response(
                jsonify("Erro interno do servidor"),
                500
            )
        
        return make_response(
            jsonify("Produto deletado com sucesso."),
            204
        )

    except AttributeError :
        return NameError