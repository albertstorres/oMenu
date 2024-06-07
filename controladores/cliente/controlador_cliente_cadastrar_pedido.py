from flask import request, make_response, jsonify
from flask_jwt_extended import get_jwt_identity

from bancodedados.modelos.Mesas import Mesas
from bancodedados.modelos.Pedidos import Pedidos

from funcoes.produtos.conferir_produtos_cadastrados import conferir_produtos_cadastrados
from funcoes.produtos.calcular_subtotais import calcular_subtotais

def cliente_cadastrar_pedido () :
    mesa = get_jwt_identity()
    req = request.get_json()
    pedido_produtos = req['pedido_produtos']

    try :

        mesa_encontrada = Mesas.select().where(Mesas.nome.contains(mesa['nome']))
        if not mesa_encontrada :
            return make_response(
                jsonify("Mesa não cadastrada."),
                404
            )
        
        array_de_produtos = map(conferir_produtos_cadastrados, pedido_produtos)
        for produto in array_de_produtos :
            if not produto :
                return make_response(
                    jsonify("Um dos produtos passados não está cadastrado.")
                )

        subtotais = map(calcular_subtotais, array_de_produtos)
        if not subtotais :
            return make_response(
                jsonify("Erro interno do servidor"),
                500                
            )
        
        valor_total_pedido = 0
        for subtotal in subtotais :
            valor_total_pedido += subtotal['subtotal']

        pedido_cadastrado = Pedidos.create(
            mesa_id=mesa_encontrada['id'],
            observacap=req['observacao'],
            valor=valor_total_pedido
        )
        if not pedido_cadastrado :
            return make_response(
                jsonify("Erro interno do servidor"),
                500
            )
        
        return make_response(
            jsonify("Pedido cadastrado com sucesso"),
            200
        )

    except AttributeError :
        return NameError