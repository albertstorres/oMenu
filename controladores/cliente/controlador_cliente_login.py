from flask import make_response, jsonify
from flask_jwt_extended import create_access_token
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
        
        token = create_access_token(identity={"nome": mesa_encontrada.nome})
        if not token :
            return make_response(
                jsonify("Erro interno do servidor"),
                500
            )

        return make_response(
            jsonify(f"token: {token}"),
            200
        )

    except AttributeError :
        return NameError
