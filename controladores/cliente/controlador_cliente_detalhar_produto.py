from flask import make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Produtos import Produtos
from bancodedados.modelos.Mesas import Mesas

def cliente_detalhar_produto (produto_id) :
    mesa = get_jwt_identity()

    try :
        mesa_encontrada = Mesas.get_or_none(Mesas.nome.contains(mesa['nome']))
        if not mesa_encontrada :
            return make_response(
                jsonify("Mesa não encontrada"),
                404
            )
        
        produto_encontrado = Produtos.select().where(Produtos.id == produto_id).dicts()
        if not produto_encontrado :
            return make_response (
                jsonify("Produto não encontrado"),
                404
            )

        return make_response(
            jsonify(list(produto_encontrado)),
            200
        )
    
    except ArithmeticError :
        return NameError 