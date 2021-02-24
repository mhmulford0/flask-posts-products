import flask
from flask import request, jsonify
from routes.products import product_blueprint
from routes.posts import post_blueprint

app = flask.Flask(__name__)
app.config['Debug'] = True

app.register_blueprint(product_blueprint, url_prefix="/product")
app.register_blueprint(post_blueprint, url_prefix="/post")
app.run()