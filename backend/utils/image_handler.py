import os
from werkzeug.utils import secure_filename
from PIL import Image
from app import app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_image(image):
    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(filepath)
        
        # Optionally resize the image
        with Image.open(filepath) as img:
            img.thumbnail((300, 300))
            img.save(filepath)
        
        return filename
    return None