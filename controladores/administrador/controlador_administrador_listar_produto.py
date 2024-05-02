from flask import  make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Categorias import Categorias
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Produtos import Produtos

def administrador_listar_produto () :
    usuario = get_jwt_identity()
    try :

        usuario_encontrado = Usuarios.get_or_none(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify({"mensagem": "Usuário não encontrado!"}),
                404
            )
        produtos = Produtos.select(Produtos).join(Categorias).group_by(Categorias.id, Produtos.id).dicts()
        print(f"LISTA DE PRODUTOS: {produtos}")
        return make_response(
            jsonify(list(produtos)),
            200
        )
    
    except ArithmeticError :
        return NameError
