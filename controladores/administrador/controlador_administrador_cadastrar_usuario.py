from flask import request, jsonify, make_response
import bcrypt
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Usuarios import Usuarios

def administrador_cadastrar_usuario () :
    req = request.get_json()
    usuario = get_jwt_identity()

    try :
    
        usuario_validado = Usuarios.get_or_none(Usuarios.username.contains(usuario['username']))
        if not usuario_validado :
            return make_response(
                jsonify("Usaário não cadastrado"),
                404
            )

        usuario_encontrado = Usuarios.select().where(Usuarios.username.contains(req['username']))
        if usuario_encontrado :
            return make_response(
                jsonify("Usuário já cadastrado"),
                404
            )

        senha_hash = bcrypt.hashpw(req['senha'].encode('UTF-8'), bcrypt.gensalt())
        print(f"SENHA HASH: {senha_hash}")

        usuario_cadastrado = Usuarios.create(
            username = req['username'],
            senha = senha_hash
            )
        if not usuario_cadastrado :
            return make_response(
                jsonify("Erro interno do servidor!"),
                500
            )
        
        return make_response(
            jsonify("Usuário cadastrado com sucesso!"),
            200
        )
    
    except AttributeError :
        return NameError