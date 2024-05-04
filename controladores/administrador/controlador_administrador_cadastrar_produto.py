from flask import request, make_response, jsonify
from flask_jwt_extended import get_jwt_identity
from bancodedados.modelos.Categorias import Categorias
from bancodedados.modelos.Usuarios import Usuarios
from bancodedados.modelos.Produtos import Produtos


def administrador_cadastrar_produto () :
    req = request.get_json()
    usuario = get_jwt_identity()

    try :

        usuario_encontrado = Usuarios.get_or_none(Usuarios.username.contains(usuario['username']))
        if not usuario_encontrado :
            return make_response(
                jsonify("Usuário não cadastrado!"),
                404
            )
        
        categoria_encontrada = Categorias.get_by_id(req['categoria_id'])
        if not categoria_encontrada :
            return make_response(
                jsonify("Categoria não cadastrada!"),
                404
            )
        
        produto_encontrado = Produtos.select().where(Produtos.nome.contains(req['nome']))
        if produto_encontrado :
            return make_response(
                jsonify("Produto já cadastrado!"),
                404
            )
        
        produto_cadastrado = Produtos.create(
            nome=req['nome'],
            detalhamento=req['detalhamento'],
            valor=req['valor'] / 100,
            categoria_id=req['categoria_id'],
            audio=req['audio'],
            imagem=req['imagem'],
            video=req['video'],
        )
        
        if not produto_cadastrado :
            return make_response(
                jsonify("Erro interno do servidor!"),
                500
            )
        
        return make_response(
            jsonify("Produto cadastrado com sucesso!"),
            200
        )
    
    except AttributeError :
        return NameError
