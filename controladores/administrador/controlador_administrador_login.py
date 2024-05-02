from flask import request, make_response, jsonify
import bcrypt
from flask_jwt_extended import create_access_token
from bancodedados.modelos.Usuarios import Usuarios
from funcoes.login.conferir_username_senha import conferir_username_senha

def administrador_login () :
    req = request.get_json()

    try :
        dados_informados = conferir_username_senha(req['username'], req['senha'])
        if not dados_informados :
            return make_response(
                jsonify("username e senha saão obrigatórios"),
                404
            )
    
        usuario_encontrado = Usuarios.get_or_none(Usuarios.username.contains(req['username']))
        if not usuario_encontrado : 
            return make_response(
                jsonify("Usuário ou senha inválidos!"),
                404
            )

        if not bcrypt.checkpw(req['senha'].encode('UTF-8'), usuario_encontrado.senha.encode('UTF-8')) :
            return make_response(
                jsonify("Usuário ou senha inválidos!"),
                404
            )
        
        token = create_access_token(identity={"username": req['username']})
        return make_response(
            jsonify(f"token: {token}"),
            200
        )
    
    except AttributeError :
        return NameError