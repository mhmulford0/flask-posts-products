from peewee import *
from models.db import db


class Product(Model):
    id = AutoField
    name = CharField()
    price = IntegerField()
    qty = IntegerField()

    class Meta:
        database = db