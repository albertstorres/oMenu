from peewee import Model, CharField
from bancodedados.bancodedados import db

class BaseModel (Model) :
    class Meta :
        database = db

class Mesas (BaseModel) :
   nome = CharField(unique=True)
   senha = CharField()

   