from peewee import Model, CharField, IntegerField, TextField, ForeignKeyField
from bancodedados.bancodedados import db
from bancodedados.modelos.Categorias import Categorias

class BaseModel (Model) :
    class Meta :
        database = db

class Produtos (BaseModel) : 
  descricao = TextField(null=False)
  valor = IntegerField (null=False)
  categoria_id = ForeignKeyField(Categorias, backref='id')
  audio = CharField()
  imagem = CharField()
  video = CharField()