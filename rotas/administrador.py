#Importação das bibliotecas
from flask import Blueprint

#Importação dos controladores
from controladores.administrador.controlador_administrador_atualizar_produto import administrador_atualizar_produto
from controladores.administrador.controlador_administrador_cadastrar_mesa import administrador_cadastrar_mesa
from controladores.administrador.controlador_administrador_cadastrar_produto import administrador_cadastrar_produto
from controladores.administrador.controlador_administrador_cadastrar_usuario import administrador_cadastrar_usuario
from controladores.administrador.controlador_administrador_deletar_produto import administrador_deletar_produto
from controladores.administrador.controlador_administrador_listar_produto import administrador_listar_produto
from controladores.administrador.controlador_administrador_login import administrador_login

#Registro da Blueprint (conjunto de rotas)
administrador_rotas = Blueprint('administrador', __name__)

#Rota de login. Faltando JWT
@administrador_rotas.route('/login', methods=['POST'])
def login () :
    return administrador_login ()
    
#Rota de criação de novo usuário. Faltando senha HASH
@administrador_rotas.route('/usuario', methods=['POST'])
def usuarioCadastrar () :
    return administrador_cadastrar_usuario ()

#Rota de criação de novas mesas. Faltando senha HASH
@administrador_rotas.route('/mesa/<int:usuario_id>', methods=['POST'])
def mesaCadastrar () :
    return administrador_cadastrar_mesa ()

#Rota de cadastro de produtos. Faltando AWS-SDK (envio de arquivos). Faltando transcrever o arquivo descrição!
@administrador_rotas.route('/produto/<int:usuario_id>', methods=['POST'])
def produtoCadastrar (usuario_id) :
    return administrador_cadastrar_produto (usuario_id)

#Rota de listar os produtos. Faltando ordenar por categoria_id
@administrador_rotas.route('/produto/<int:usuario_id>', methods=['GET'])
def produtoListar (usuario_id) :
    return administrador_listar_produto (usuario_id)

#Rota de excluir um produto.
@administrador_rotas.route('/produto/<int:usuario_id>', methods=['DELETE'])
def produtoDeletar (usuario_id) :
    return administrador_deletar_produto (usuario_id)

#Rota de atualizar um produto. Faltando melhorar o cadastro apenas do que se deseja atualizar
@administrador_rotas.route('/produto/<int:usuario_id>', methods=['PUT'])
def produtoAtualizar (usuario_id) :
    return administrador_atualizar_produto (usuario_id)