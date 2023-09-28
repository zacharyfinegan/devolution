from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/generic_posts')
def get_generic_posts():
    generic_posts = [
        {"id": 1, "title": "generic post 1", "content": "this is generic 1"},
        {"id": 2, "title": "generic post 2", "content": "this is generic 2"}
    ]
    data = {"generic": generic_posts} #jsonify? return jsonify(generic_posts)
    return data

@app.route('/api/something_new')
def get_something_new():
    something_new = [
        {'name': 'newness'},
        {'name': 'other newness'}
    ]
    return {'something_new': something_new}