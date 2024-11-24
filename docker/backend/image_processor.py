import os
from PIL import Image
from werkzeug.utils import secure_filename

class ImageProcessor:
    def process_image(self, file):
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1].lower()
        
        # Open image to get dimensions
        image = Image.open(file)
        width, height = image.size
        
        return {
            'filename': filename,
            'extension': extension[1:],  # Remove the dot from extension
            'width': width,
            'height': height,
            'size_kb': len(file.read()) / 1024
        }