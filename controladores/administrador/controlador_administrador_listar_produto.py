from flask import request, make_response, jsonify
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Produtos import Produtos

def administrador_listar_produto (usuario_id) :
    administrador_encontrado = Usuarios.get_by_id(usuario_id)
    if not administrador_encontrado :
        return make_response(
            jsonify({"mensagem": "Administrador não encontrado!"}),
            404
        )
    produtos = Produtos.select().dicts()
    print(f"LISTA DE PRODUTOS: {produtos}")
    return make_response(
        jsonify(list(produtos)),
        200
    )
