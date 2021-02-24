from peewee import *

db = SqliteDatabase('app.db')

class Post(Model):
    id = AutoField()
    title = CharField()
    content = CharField()

    class Meta:
        database = db
