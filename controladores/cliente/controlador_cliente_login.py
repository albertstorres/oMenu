from flask import make_response, jsonify
from bancodedados.modelos.Mesas import Mesas

def cliente_login (mesa_nome, mesa_senha) :
    mesa_encontrada = Mesas.get(Mesas.nome.contains(mesa_nome))
    if not mesa_encontrada :
        return make_response(
            jsonify("Mesa não encontrada"),
            404
        )
    print(f"MESA ENCONTRADA: {mesa_encontrada}")
    if mesa_encontrada.senha != mesa_senha :
        return make_response(
            jsonify("Username ou senha inválidos"),
            404
        )
    return make_response(
        jsonify("Mesa logada"),
        200
    )
