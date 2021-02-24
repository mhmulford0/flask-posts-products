from peewee import *
from models.Posts import Post
from models.Product import Product

db = SqliteDatabase('app.db')

db.create_tables([Product, Post])