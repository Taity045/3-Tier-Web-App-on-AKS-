from flask import Blueprint, request, jsonify
from models.post import Post
from app import db
from services.post_service import create_post, get_all_posts, get_post_by_id
from utils.image_handler import save_image

bp = Blueprint('posts', __name__, url_prefix='/api/posts')

@bp.route('', methods=['POST'])
def create_new_post():
    data = request.form
    image = request.files.get('image')
    
    if image:
        image_filename = save_image(image)
    else:
        image_filename = None
    
    new_post = create_post(data['title'], data['content'], image_filename)
    return jsonify(new_post.to_dict()), 201

@bp.route('', methods=['GET'])
def get_posts():
    posts = get_all_posts()
    return jsonify([post.to_dict() for post in posts])

@bp.route('/<int:id>', methods=['GET'])
def get_post(id):
    post = get_post_by_id(id)
    if post:
        return jsonify(post.to_dict())
    return jsonify({'error': 'Post not found'}), 404