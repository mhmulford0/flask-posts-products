from flask import Blueprint, jsonify, g
from models.Posts import Post
from flask_expects_json import expects_json
from models.db import db

post_blueprint = Blueprint('posts', __name__)

schema = {
    'type': 'object',
    'properties': {
        'title': {'type': 'string'},
        'content': {'type': 'string'},
    },
    'required': ['title', 'content']
}

@post_blueprint.route('/', methods=['POST'])
@expects_json(schema)
def index():

    title = g.data['title']
    content = g.data['content']

    new_post = Post.create(title=title, content=content)
    new_post.save()
    
    db.close()

    return {"msg": "New post added"}, 201

@post_blueprint.route('/', methods=['GET'])
def get_all_posts():

    all_posts = []
    for post in Post.select():
        all_posts.append({'id': post.id, 'title': post.title, 'content': post.content})
    
    db.close()

    return jsonify(all_posts), 200

@post_blueprint.route('/<int:id>', methods=['GET'])
def get_one_post(id):
    one_post = {} 
    for post in Post.select().where(Post.id == id):
        one_post.update({'id': post.id, 'title': post.title, 'content': post.content})
    
    db.close()

    return one_post

@post_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_post(id):

    try:
        post = Post.get(Post.id == id)
        post.delete_instance()
        return {"msg": "post deleted"}, 200
    except:
        return {"error": "post does not exists"}, 400

   