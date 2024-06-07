from flask import request, make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Produtos import Produtos
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Categorias import Categorias

def administrador_atualizar_produto () :
    req = request.get_json()
    usuario = get_jwt_identity()

    try :
        
        usuario_encontrado = Usuarios.select().where(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário não encontrado"),
                404
            )
        
        produto_encontrado = Produtos.get_by_id(req['produto_id'])
        if not produto_encontrado :
            return make_response(
                jsonify("Produto não encontrado."),
                404
            )
        
        categoria_encontrada = Categorias.get_by_id(req['categoria_id'])
        if not categoria_encontrada :
            return make_response(
                jsonify("Categoria não encontrada"),
                404
            )
        
        produto_encontrado.descricao = req['descricao']
        produto_encontrado.valor = req['valor']
        produto_encontrado.categoria_id = req['categoria_id']
        produto_encontrado.audio = req['audio']
        produto_encontrado.imagem = req['imagem']
        produto_encontrado.video = req['video']
        produto_encontrado.save()

        return make_response(
            jsonify("Produto atuakizado com sucesso."),
            201
        )
    
    except AttributeError :
        return NameError
    