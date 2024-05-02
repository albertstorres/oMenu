from flask import make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Produtos import Produtos

def administrador_detalhar_produto (produto_id) :
    usuario = get_jwt_identity()

    try :

        usuario_encontrado = Usuarios.get_or_none(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário não encontrado"),
                404
            )
        
        produto_encontrado = Produtos.select().where(Produtos.id == produto_id).dicts()
        if not produto_encontrado :
            return make_response(
                jsonify("Produto não encontrado"),
                404
            )
        
        return make_response(
            jsonify(list(produto_encontrado))
        )

    except AttributeError :
        return NameError