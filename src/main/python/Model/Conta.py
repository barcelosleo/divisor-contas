import peewee

from .BaseModel import BaseModel
from .RegistroMensal import RegistroMensal
from .Morador import Morador
from .TipoConta import TipoConta

class Conta(BaseModel):
    id = peewee.PrimaryKeyField()
    data = peewee.DateField()
    valor = peewee.FloatField()
    descricao = peewee.CharField(null=True)

    registro_mensal = peewee.ForeignKeyField(RegistroMensal)
    morador = peewee.ForeignKeyField(Morador, null=True)
    tipo_conta = peewee.ForeignKeyField(TipoConta)