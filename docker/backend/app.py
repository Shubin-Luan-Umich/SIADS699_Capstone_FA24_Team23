from flask import Flask, request, jsonify
from flask_cors import CORS
from image_processor import ImageProcessor
from feedback_handler import FeedbackHandler
from lipstick_recommender import LipstickRecommender
import cv2
import numpy as np

app = Flask(__name__)
CORS(app)

# Initialize handlers
feedback_handler = FeedbackHandler()
feedback_handler.init_db()
recommender = LipstickRecommender()

@app.route('/upload', methods=['POST'])
def upload_image():
    """Handle image upload and generate recommendations"""
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        file_content = file.read()
        if not file_content:
            return jsonify({'error': 'Empty file'}), 400

        nparr = np.frombuffer(file_content, np.uint8)
        if len(nparr) == 0:
            return jsonify({'error': 'Invalid image data'}), 400

        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if image is None:
            return jsonify({'error': 'Failed to decode image'}), 400

        result = recommender.get_recommendations(image)

        file.seek(0)

        image_info = ImageProcessor.process_image(file)

        response = {
            'image_info': image_info,
            'cluster_info': {
                'id': result.cluster_id,
                'name': result.cluster_name,
                'price_range': result.price_range
            },
            'recommendations': result.recommendations
        }

        return jsonify(response)

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    """Get recommendations with specific filters"""
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    try:
        # Get parameters
        sort_by = request.form.get('sort_by', 'color_similarity')
        n_recommendations = int(request.form.get('n_recommendations', 10))
        min_price = float(request.form.get('min_price')) if request.form.get('min_price') else None
        max_price = float(request.form.get('max_price')) if request.form.get('max_price') else None
        
        # Process image
        file = request.files['image']
        file_bytes = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        # Get recommendations
        result = recommender.get_recommendations(
            image=image,
            sort_by=sort_by,
            n_recommendations=n_recommendations,
            min_price=min_price,
            max_price=max_price
        )
        
        return jsonify({
            'cluster_info': {
                'id': result.cluster_id,
                'name': result.cluster_name,
                'price_range': result.price_range
            },
            'recommendations': result.recommendations
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['POST'])
def save_feedback():
    """Save user feedback"""
    data = request.json
    try:
        feedback_handler.save_feedback(
            data.get('image_name'),
            data.get('rating'),
            data.get('feedback')
        )
        return jsonify({'message': 'Feedback saved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
