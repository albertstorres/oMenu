from peewee import Model, CharField
from bancodedados.bancodedados import db

class BaseModel (Model) :
    class Meta :
        database = db

class Categorias (BaseModel) :
    descricao = CharField(null=False)