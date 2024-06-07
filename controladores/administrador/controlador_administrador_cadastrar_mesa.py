from flask import request, make_response, jsonify
import bcrypt
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Mesas import Mesas


def administrador_cadastrar_mesa () :
    req = request.get_json()
    usuario = get_jwt_identity()
    
    try:

        usuario_encontrado = Usuarios.get_or_none(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário não cadastrado"),
                404
            )

        mesa_encontrada = Mesas.select().where(Mesas.nome == req['nome'])
        if mesa_encontrada :
            return make_response(
                jsonify("Mesa já cadastrada"),
                404
            )
        
        senha_hash = bcrypt.hashpw(req['senha'].encode('UTF-8'), bcrypt.gensalt())

        mesa_cadastrada = Mesas.create(
            nome = req['nome'],
            senha = senha_hash
        )
        if not mesa_cadastrada :
            return make_response(
                jsonify("Erro interno do servidor"),
                500
            )

        return make_response(
            jsonify("Mesa cadastrada com sucesso"),
            200
        )
    
    except AttributeError :
        return NameError