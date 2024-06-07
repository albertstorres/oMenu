from peewee import Model, CharField, IntegerField, TextField, ForeignKeyField
from bancodedados.bancodedados import db
from bancodedados.modelos.Categorias import Categorias

class BaseModel (Model) :
    class Meta :
        database = db

class Produtos (BaseModel) : 
  nome = CharField(null=False)
  detalhamento = TextField(null=False)
  valor = IntegerField (null=False)
  categoria_id = ForeignKeyField(Categorias, backref='produtos')
  imagem = CharField()
  video = CharField()
  