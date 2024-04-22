from flask import make_response, jsonify
from bancodedados.modelos.Mesas import Mesas
from bancodedados.modelos.Produtos import Produtos

def cliente_listar_produto (mesa_id) :
    mesa_encontrada = Mesas.get_by_id(mesa_id)
    if not mesa_encontrada :
        return make_response(
            jsonify("Mesa não encontrada"),
            404
        )
    produtos = Produtos.select().dicts()
    return make_response(
        jsonify(list(produtos)),
        200
    )