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
    subtotais = []
    valor_total_pedido = 0

    try :
        if len(pedido_produtos) < 1 :
            return make_response(
                jsonify("Para cadastrar um pedido, precisa adicionar ao menos um produto."),
                404
            )
        
        mesa_encontrada = Mesas.select().where(Mesas.nome.contains(mesa['nome']))
        if not mesa_encontrada :
            return make_response(
                jsonify("Mesa não cadastrada."),
                404
            )
        
      
        conferir_produtos_cadastrados(pedido_produtos)
       
        calcular_subtotais(pedido_produtos, subtotais)
    
        for subtotal in subtotais :
            valor_total_pedido += subtotal['subtotal']

        pedido_cadastrado = Pedidos.create(
            mesa_id=req['mesa_id'],
            observacao=req['observacao'],
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