#Importação das bibliotecas
from flask import Blueprint

#Importação dos controladores
from controladores.cliente.controlador_cliente_login import cliente_login
from controladores.cliente.controlador_cliente_listar_produto import cliente_listar_produto

cliente_rotas = Blueprint('cliente', __name__)

# Rota de login das mesas. Faltando JWT
@cliente_rotas.route('/loginCliente/<string:mesa_nome>&<string:mesa_senha>', methods = ['POST'])
def login (mesa_nome, mesa_senha) :
    return cliente_login (mesa_nome, mesa_senha)

#Rota para listagem do cardápio. Faltando ordenar por categoria_id
@cliente_rotas.route('/cardapio/<int:mesa_id>', methods=['GET'])
def cardapio (mesa_id) :
    return cliente_listar_produto (mesa_id)


#Rota fazer pedido
