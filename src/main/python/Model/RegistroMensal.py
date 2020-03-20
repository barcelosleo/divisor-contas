import peewee

from .BaseModel import BaseModel

class RegistroMensal(BaseModel):
    id = peewee.PrimaryKeyField()
    data = peewee.DateField()
    total = peewee.FloatField()
    numero_pessoas = peewee.IntegerField()