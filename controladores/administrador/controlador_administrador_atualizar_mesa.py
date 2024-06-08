from flask import request, make_response, jsonify
import bcrypt
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Mesas import Mesas
from bancodedados.modelos.Usuarios import Usuarios

def administrador_atualizar_mesa () :
    req = request.get_json()
    usuario = get_jwt_identity()

    try :

        usuario_encontrado = Usuarios.select().where(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário não cadastrado"),
                404
            )
        
        mesa_encontrada = Mesas.get_by_id(req['mesa_id'])
        if not mesa_encontrada :
            return make_response(
                jsonify("Mesa não cadastrada"),
                404
            )
        
        senha_hash = bcrypt.hashpw(req['mesa_senha'].encode('UTF-8'), bcrypt.gensalt())

        mesa_encontrada.nome = req['mesa_nome']
        mesa_encontrada.senha = senha_hash
        mesa_encontrada.save()

        return make_response(
            jsonify("Mesa atualizada com sucesso"),
            201
        )


    except AttributeError :
        return NameError
