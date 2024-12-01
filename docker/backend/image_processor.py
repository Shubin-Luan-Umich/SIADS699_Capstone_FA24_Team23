import os
from PIL import Image
import numpy as np
from io import BytesIO
from werkzeug.utils import secure_filename
import cv2
import base64

class ImageProcessor:
    """Handles image processing operations for the lipstick recommendation system."""
    
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
    
    @staticmethod
    def allowed_file(filename: str) -> bool:
        """Check if file extension is allowed.

        Args:
            filename: Name of the uploaded file
            
        Returns:
            bool: True if file extension is allowed
        """
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ImageProcessor.ALLOWED_EXTENSIONS
    
    @staticmethod
    def validate_image_size(file) -> bool:
        """Check if file size is within limits.
        
        Args:
            file: File object to check
            
        Returns:
            bool: True if file size is acceptable
        """
        file.seek(0, os.SEEK_END)
        size = file.tell()
        file.seek(0)
        return size <= ImageProcessor.MAX_IMAGE_SIZE
    
    @staticmethod
    def process_image(file) -> dict:
        """Process uploaded image and return image information.
        
        Args:
            file: Uploaded file object
            
        Returns:
            dict: Image information including dimensions and format
        
        Raises:
            ValueError: If file is invalid or processing fails
        """
        if not file or not file.filename:
            raise ValueError("No file provided")
            
        if not ImageProcessor.allowed_file(file.filename):
            raise ValueError("Invalid file format. Allowed formats: PNG, JPG, JPEG")
            
        if not ImageProcessor.validate_image_size(file):
            raise ValueError(f"File too large. Maximum size: {ImageProcessor.MAX_IMAGE_SIZE/1024/1024}MB")
        
        try:
            # Read image
            image_bytes = file.read()
            image = Image.open(BytesIO(image_bytes))
            
            # Get basic information
            width, height = image.size
            format_ext = image.format.lower()
            
            # Convert to RGB if necessary
            if image.mode not in ('RGB', 'L'):
                image = image.convert('RGB')
            
            # Calculate file size in KB
            size_kb = len(image_bytes) / 1024
            
            # Generate thumbnail for preview if needed
            thumbnail_base64 = None
            if max(width, height) > 800:
                image.thumbnail((800, 800), Image.LANCZOS)
                thumbnail_buffer = BytesIO()
                image.save(thumbnail_buffer, format='JPEG')
                thumbnail_base64 = base64.b64encode(thumbnail_buffer.getvalue()).decode()
            
            return {
                'filename': secure_filename(file.filename),
                'format': format_ext,
                'width': width,
                'height': height,
                'size_kb': size_kb,
                'aspect_ratio': width/height,
                'thumbnail': thumbnail_base64 if thumbnail_base64 else None,
                'mode': image.mode
            }
            
        except Exception as e:
            raise ValueError(f"Error processing image: {str(e)}")
    
    @staticmethod
    def prepare_image_for_analysis(file) -> np.ndarray:
        """Prepare image for facial analysis.
        
        Args:
            file: Uploaded file object
            
        Returns:
            np.ndarray: Image array ready for analysis
        """
        # Read image bytes
        image_bytes = np.frombuffer(file.read(), np.uint8)
        file.seek(0)  # Reset file pointer
        
        # Decode image
        image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
        
        # Basic image preprocessing
        if image is None:
            raise ValueError("Failed to decode image")
            
        # Resize if too large
        max_dimension = 1024
        height, width = image.shape[:2]
        if max(height, width) > max_dimension:
            scale = max_dimension / max(height, width)
            image = cv2.resize(image, None, fx=scale, fy=scale, 
                             interpolation=cv2.INTER_AREA)
        
        return image
    
    @staticmethod
    def encode_image_to_base64(image: np.ndarray, format: str = 'JPEG') -> str:
        """Convert image array to base64 string.
        
        Args:
            image: Image array
            format: Output image format
            
        Returns:
            str: Base64 encoded image string
        """
        success, buffer = cv2.imencode(f'.{format.lower()}', image)
        if not success:
            raise ValueError("Failed to encode image")
            
        return base64.b64encode(buffer).decode()
