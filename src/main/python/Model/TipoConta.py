import peewee

from .BaseModel import BaseModel

class TipoConta(BaseModel):
    id = peewee.PrimaryKeyField()
    data = peewee.DateField()
    nome = peewee.CharField()