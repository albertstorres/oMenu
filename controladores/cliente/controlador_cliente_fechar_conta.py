from flask import request, make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Mesas import Mesas
from bancodedados.modelos.Pedidos import Pedidos

def cliente_fechar_conta (mesa_id) :
    mesa = get_jwt_identity()
    req = request.get_json()
    total = 0
    array_pedidos = req['array_pedidos']
    try :

        mesa_encontrada = Mesas.select().where(Mesas.nome.contains(mesa['nome'])).dicts()
        if not mesa_encontrada :
            return make_response(
                jsonify("Mesa não cadastrada."),
                404
            )
        print(f"ID DA MESA ENCONTRADA: {mesa_encontrada['id']}")
        mesa_encontrada_id = {
            "id": mesa_encontrada['id']
        }
        if mesa_encontrada_id['id'] != mesa_id :
            return make_response(
                jsonify("Não é possivel fechar a conta de outra mesa!"),
                404
            )

        print('PASSA DA VALIDAÇÃO DA MESA QUE FECHA A CONTA')
        for pedidos_abertos in req['array_pedidos'] :
            pedidos_abertos = Pedidos.select.where((Pedidos.mesa_id == mesa_id) & (Pedidos.finalizado == False)).dicts()
        print('PASSA DOS PEDIDOS EM ABERTOS DA MESA')
        for pedido_aberto in pedidos_abertos :
            total += pedido_aberto.valor
        print('PASSA DO VALOR TOTAL')
        for pedido_aberto in pedidos_abertos :
            pedido_aberto.finalizado=True
        print('PASSA DA MUDANÇA DE STATUS DE FINALIZADO')
        return make_response(
            jsonify(total),
            200
        )

    except AttributeError:
        return NameError
