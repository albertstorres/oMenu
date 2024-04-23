from flask import make_response, jsonify
import bcrypt
from bancodedados.modelos.Mesas import Mesas

def cliente_login (mesa_nome, mesa_senha) :
    try: 

        mesa_encontrada = Mesas.get(Mesas.nome.contains(mesa_nome))
        if not mesa_encontrada :
            return make_response(
                jsonify("Mesa não encontrada"),
                404
            )

        if not bcrypt.checkpw(mesa_senha.encode('UTF-8'), mesa_encontrada.senha.encode('UTF-8')) :
            return make_response(
                jsonify("Username ou senha inválidos"),
                404
            )
        return make_response(
            jsonify("Mesa logada"),
            200
        )

    except AttributeError :
        return NameError
