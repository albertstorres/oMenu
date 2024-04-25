from flask import make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Mesas import Mesas
from bancodedados.modelos.Produtos import Produtos

def cliente_listar_produto () :
    mesa = get_jwt_identity()
    
    try :

        mesa_encontrada = Mesas.get_or_none(Mesas.nome.contains(mesa['nome']))
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

    except ArithmeticError :
        return NameError