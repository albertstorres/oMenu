from flask import make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Pedidos import Pedidos
from bancodedados.modelos.Usuarios import Usuarios

def administrador_detalhar_pedido (pedido_id) :
    usuario = get_jwt_identity()

    try :

        usuario_encontrado = Usuarios.select().where(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário não cadastrado."),
                404
            )

        pedido_encontrado = Pedidos.select().where(Pedidos.id == pedido_id).dicts()
        if not pedido_encontrado :
            return make_response(
                jsonify("Pedido não cadastrado"),
                404
            )

        return make_response(
            jsonify(list(pedido_encontrado)),
            200
        )

    except AttributeError :
        return NameError