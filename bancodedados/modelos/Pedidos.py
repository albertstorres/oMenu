from peewee import Model, IntegerField, TextField, ForeignKeyField
from bancodedados.bancodedados import db
from bancodedados.modelos.Mesas import Mesas

class BaseModel (Model) :
    class Meta :
        database = db

class Pedidos (BaseModel) :
    mesa_id = ForeignKeyField(Mesas, backref='pedidos')
    observacao = TextField
    valor = IntegerField(null=False)
