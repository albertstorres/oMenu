from rotas.administrador import administrador_rotas
from rotas.cliente import cliente_rotas
from bancodedados.bancodedados import db




def configure_all (app) :
    configure_rotas(app)
    configure_db()

def configure_rotas (app) :
    app.register_blueprint(administrador_rotas)
    app.register_blueprint(cliente_rotas)

def configure_db () :
    db.connect()
    