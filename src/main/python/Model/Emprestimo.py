import peewee

from .BaseModel import BaseModel
from .RegistroMensal import RegistroMensal
from .Morador import Morador

class Emprestimo(BaseModel):
    id = peewee.PrimaryKeyField()
    data = peewee.DateField()
    valor = peewee.FloatField()
    descricao = peewee.CharField()

    registro_mensal = peewee.ForeignKeyField(RegistroMensal)
    de = peewee.ForeignKeyField(Morador)
    para = peewee.ForeignKeyField(Morador)