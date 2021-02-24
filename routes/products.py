from flask import Blueprint
from models.Product import Product

product_blueprint = Blueprint('products', __name__)

@product_blueprint.route('/')
def index():
    new_product = Product.create(name="Test", price=100, qty=5)
    new_product.save()
    return {"hello": "world"}, 202

@product_blueprint.route('/one')
def get_products():
    for product in Product.select():
        print(product.name, product.price)
    return {"msg": "sucess"}, 200