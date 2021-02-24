from flask import Blueprint, jsonify, g
from models.Posts import Post
from flask_expects_json import expects_json

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

    return {"msg": "New post added"}, 201

@post_blueprint.route('/', methods=['GET'])
def get_posts():

    all_posts = []
    for post in Post.select():
        all_posts.append({'id': post.id, 'title': post.title, 'content': post.content})

    return jsonify(all_posts), 200