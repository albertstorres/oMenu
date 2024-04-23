import os
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from rotas.administrador import administrador_rotas
from rotas.cliente import cliente_rotas
from bancodedados.bancodedados import db

load_dotenv()


def configure_all (app) :
    configure_rotas(app)
    configure_db()
    configure_jwt(app)


def configure_rotas (app) :
    app.register_blueprint(administrador_rotas)
    app.register_blueprint(cliente_rotas)

def configure_db () :
    db.connect()

def configure_jwt (app) :
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    jwt = JWTManager(app)