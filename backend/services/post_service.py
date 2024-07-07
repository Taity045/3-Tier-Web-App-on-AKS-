from models.post import Post
from app import db

def create_post(title, content, image_filename=None):
    new_post = Post(title=title, content=content, image_filename=image_filename)
    db.session.add(new_post)
    db.session.commit()
    return new_post

def get_all_posts():
    return Post.query.order_by(Post.created_at.desc()).all()

def get_post_by_id(id):
    return Post.query.get(id)