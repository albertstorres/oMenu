from flask import request, jsonify, make_response
from bancodedados.modelos.Usuarios import Usuarios

def administrador_cadastrar_usuario () :
    req = request.get_json()
    
    usuario_encontrado = Usuarios.select().where(Usuarios.username.contains(req['username']))
    if usuario_encontrado :
        return make_response(
            jsonify("Usaário já cadastrado"),
            404
        )

    usuario_cadastrado = Usuarios.create(
        username = req['username'],
        senha = req['senha']
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