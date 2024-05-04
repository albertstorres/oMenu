#Importação das bibliotecas
from flask import Blueprint
from flask_jwt_extended import jwt_required

#Importação dos controladores
from controladores.administrador.controlador_administrador_atualizar_produto import administrador_atualizar_produto
from controladores.administrador.controlador_administrador_cadastrar_mesa import administrador_cadastrar_mesa
from controladores.administrador.controlador_administrador_cadastrar_produto import administrador_cadastrar_produto
from controladores.administrador.controlador_administrador_cadastrar_usuario import administrador_cadastrar_usuario
from controladores.administrador.controlador_administrador_deletar_produto import administrador_deletar_produto
from controladores.administrador.controlador_administrador_detalhar_produto import administrador_detalhar_produto
from controladores.administrador.controlador_administrador_listar_produto import administrador_listar_produto
from controladores.administrador.controlador_administrador_login import administrador_login

#Registro da Blueprint (conjunto de rotas)
administrador_rotas = Blueprint('administrador', __name__)

#Rota de login. [COMPLETA]
@administrador_rotas.route('/login', methods=['POST'])
def login () :
    return administrador_login ()
    
#Rota de criação de novo usuário. [COMPLETA]
@administrador_rotas.route('/usuario', methods=['POST'])
@jwt_required()
def usuarioCadastrar () :
    return administrador_cadastrar_usuario ()

#Rota de criação de novas mesas. [COMPLETA]
@administrador_rotas.route('/mesa/', methods=['POST'])
@jwt_required()
def mesaCadastrar () :
    return administrador_cadastrar_mesa ()

#Rota de cadastro de produtos. Faltando AWS-SDK (envio de arquivos). Faltando transcrever o arquivo descrição!
@administrador_rotas.route('/produto/', methods=['POST'])
@jwt_required()
def produtoCadastrar () :
    return administrador_cadastrar_produto ()

#Rota de listar os produtos. Faltando ordenar por categoria_id
@administrador_rotas.route('/produtos/', methods=['GET'])
@jwt_required()
def produtoListar () :
    return administrador_listar_produto ()

@administrador_rotas.route('/produto/<int:produto_id>', methods=['GET'])
@jwt_required()
def produtoDetalhar (produto_id) :
    return administrador_detalhar_produto (produto_id)

#Rota de excluir um produto.
@administrador_rotas.route('/produto/', methods=['DELETE'])
@jwt_required()
def produtoDeletar () :
    return administrador_deletar_produto ()

#Rota de atualizar um produto. Faltando melhorar o cadastro apenas do que se deseja atualizar
@administrador_rotas.route('/produto/<int:usuario_id>', methods=['PUT'])
@jwt_required()
def produtoAtualizar (usuario_id) :
    return administrador_atualizar_produto (usuario_id)