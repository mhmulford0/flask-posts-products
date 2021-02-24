from peewee import *
from models.db import db

class Post(Model):
    id = AutoField()
    title = CharField()
    content = CharField()

    class Meta:
        database = db
