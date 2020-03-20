import peewee

db = peewee.SqliteDatabase('__local.db')

class BaseModel(peewee.Model):

    class Meta:
        database = db