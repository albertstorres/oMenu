#Importação das bibliotecas
from flask import Blueprint
from flask_jwt_extended import jwt_required

#Importação dos controladores
from controladores.cliente.controlador_cliente_cadastrar_pedido import cliente_cadastrar_pedido
from controladores.cliente.controlador_cliente_detalhar_produto import cliente_detalhar_produto
from controladores.cliente.controlador_cliente_fechar_conta import cliente_fechar_conta
from controladores.cliente.controlador_cliente_login import cliente_login
from controladores.cliente.controlador_cliente_listar_produto import cliente_listar_produto


cliente_rotas = Blueprint('cliente', __name__)

# Rota de login das mesas. [COMPLETA]
@cliente_rotas.route('/loginCliente/<string:mesa_nome>&<string:mesa_senha>', methods = ['POST'])
def login (mesa_nome, mesa_senha) :
    return cliente_login (mesa_nome, mesa_senha)

# Rota para cadastro de pedidos.
@cliente_rotas.route('/pedido/', methods = ['POST'])
@jwt_required ()
def pedido () :
    return cliente_cadastrar_pedido ()

#Rota para listagem do cardápio. Faltando ordenar por categoria_id
@cliente_rotas.route('/cardapio/', methods=['GET'])
@jwt_required()
def cardapio () :
    return cliente_listar_produto ()

#Rota detalhar pedido.
@cliente_rotas.route('/produtoDetalhado/<int:produto_id>', methods=['GET'])
@jwt_required()
def detalharProduto (produto_id) : 
    return cliente_detalhar_produto (produto_id)


#Rota fachar conta
@cliente_rotas.route('/fecharConta/<int:mesa_id>', methods=['GET'])
@jwt_required()
def fecharConta (mesa_id) :
    return cliente_fechar_conta (mesa_id)
