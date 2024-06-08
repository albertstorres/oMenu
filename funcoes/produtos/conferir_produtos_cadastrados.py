from flask import make_response, jsonify
from bancodedados.modelos.Produtos import Produtos

def conferir_produtos_cadastrados (array_de_produtos) :
    try :
        for produto in array_de_produtos :
            produto_encontrado = Produtos.get_or_none(Produtos.id == produto['produto_id'])
            if not produto_encontrado :
                return make_response(
                    jsonify("Um dos produtos passados não está cadastrado."),
                    404
                )

    except AttributeError :
        return NameError