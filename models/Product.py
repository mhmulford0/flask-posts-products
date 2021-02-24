from peewee import *

db = SqliteDatabase('app.db')

class Product(Model):
    id = AutoField
    name = CharField()
    price = IntegerField()
    qty = IntegerField()

    class Meta:
        database = db