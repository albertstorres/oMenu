from peewee import Model, CharField, IntegerField, TextField
from bancodedados.bancodedados import db

class BaseModel (Model) :
    class Meta :
        database = db

class Produtos (BaseModel) : 
  nome = CharField(null=False)
  detalhamento = TextField(null=False)
  valor = IntegerField (null=False)
  categoria_id = IntegerField()
  audio = CharField()
  imagem = CharField()
  video = CharField()
  