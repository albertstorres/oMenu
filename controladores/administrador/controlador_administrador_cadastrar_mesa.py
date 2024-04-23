from flask import request, make_response, jsonify
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Mesas import Mesas


def administrador_cadastrar_mesa (usuario_id) :
    req = request.get_json()
    if not req['nome'] or not req['senha'] :
        return make_response(
            jsonify("Nome e senha da mesa, são obrigatórios."),
            404
        )
    
    administrador_encontrado = Usuarios.get_by_id(usuario_id)
    if not administrador_encontrado :
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
    
    mesa_cadastrada = Mesas.create(
        nome = req['nome'],
        senha = req['senha']
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
