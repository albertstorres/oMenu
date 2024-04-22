from flask import request,make_response,jsonify
from bancodedados.modelos.Usuarios import Usuarios
from funcoes.login.conferir_dados_req_login import conferir_dados_req_login

def administrador_login () :
    req = request.get_json()
    dados_informados = conferir_dados_req_login(req['username'], req['senha'])
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
    
    if not usuario_encontrado.senha == req['senha'] :
        return make_response(
            jsonify("Usuário ou senha inválidos!"),
            404
        )
    
    return make_response(
        jsonify("Usuário logado!")
    )