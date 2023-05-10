from datetime import datetime

from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()

posts = [
    {
        "id": 1,
        "title": "Ads #1",
        "description": "GET, POST routes",
        "created": datetime.utcnow(),
        "owner": "user_id"
    },
    {
        "id": 2,
        "title": "Ads #2",
        "description": "PUT, DELETE routes",
        "created": datetime.utcnow(),
        "owner": "user_id"
    }
]


@app.route('/posts', methods=['GET'])
def get_list_posts():
    return jsonify(posts)


@app.route('/posts', methods=['POST'])
def add_post():
    new_post = request.json
    posts.append(new_post)
    return jsonify(posts)


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    item = next((x for x in posts if x['id'] == post_id), None)
    params = request.json
    if not item:
        return {'message': 'no post with this id'}, 400
    item.update(params)
    return item


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    idx, _ = next((x for x in enumerate(posts) if x[1]['id'] == post_id), (None, None))
    posts.pop(idx)
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)