import peewee

from .BaseModel import BaseModel

class Morador(BaseModel):
    id = peewee.PrimaryKeyField()
    data = peewee.DateField()
    nome = peewee.CharField()
    deleted = peewee.BooleanField(default=False)