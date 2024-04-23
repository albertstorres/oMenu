from flask import request,make_response,jsonify
import bcrypt
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
    
        usuario_encontrado = Usuarios.get(Usuarios.username.contains(req['username']))
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
        
        return make_response(
            jsonify("Usuário logado!")
        )
    except AttributeError :
        return NameError