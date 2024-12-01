from flask import Flask, request, jsonify
from flask_cors import CORS
from image_processor import ImageProcessor
from feedback_handler import FeedbackHandler
from lipstick_recommender import LipstickRecommender
import cv2
import numpy as np
import tempfile

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
    print("1", flush=True)
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    print("2", flush=True)
    try:
        file_content = file.read()
        if not file_content:
            return jsonify({'error': 'Empty file'}), 400
        print("3", flush=True)
        nparr = np.frombuffer(file_content, np.uint8)
        if len(nparr) == 0:
            return jsonify({'error': 'Invalid image data'}), 400
        print("4", flush=True)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if image is None:
            return jsonify({'error': 'Failed to decode image'}), 400
        print("5", flush=True)
        result = recommender.get_recommendations(image)
        print("6", flush=True)
        # print(result, flush=True)
        print("===========", flush=True)
        file.seek(0)
        print("7", flush=True)
        image_info = ImageProcessor.process_image(file)
        print("8", flush=True)
        # response = {
        #     'image_info': image_info,
        #     'cluster_info': {
        #         'id': result.cluster_id,
        #         'name': result.cluster_name,
        #         'price_range': result.price_range
        #     },
        #     'recommendations': result.recommendations
        # }
        response = {
            'image_info': image_info,
            'cluster_info': {
                'id': int(result.cluster_id),
                'name': result.cluster_name,
                'price_range': {
                    'min': float(result.price_range['min']),
                    'max': float(result.price_range['max'])
                }
            },
            'recommendations': [
                {k: float(v) if isinstance(v, (np.floating, np.float64, np.float32)) else
                    int(v) if isinstance(v, (np.integer, np.int64, np.int32)) else v
                    for k, v in rec.items()}
                for rec in result.recommendations
            ]
        }
        print("9", flush=True)
        # print(response, flush=True)
        # print(response, flush=True)
        return jsonify(response)

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    """Get recommendations with specific filters"""
    if 'image' not in request.files:
        print("20", flush=True)
        return jsonify({'error': 'No image provided'}), 400
    
    try:
        # Get parameters
        # sort_by = request.form.get('sort_by', 'color_similarity')
        print("21", flush=True)
        sort_by = request.form.get('sort_by', 'recommendation_score')
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
        # print(result.cluster_id, flush=True)
        # print(result.cluster_name, flush=True)
        # print(result.price_range, flush=True)
        # temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8')
        # temp_file.write(str(result))
        # temp_file.flush()
        # temp_file.close()
        # print(f"临时文件已保存到：{temp_file.name}")
        # print(result, flush=True)
        # clean_recommendations = convert_numpy_types(result.recommendations)
        print("522", flush=True)
        # response = {
        #     'cluster_info': {
        #         'id': result.cluster_id,
        #         'name': result.cluster_name,
        #         'price_range': result.price_range
        #     },
        #     'recommendations': [
        #         {k: float(v) if isinstance(v, (np.floating, np.float64, np.float32)) else
        #             int(v) if isinstance(v, (np.integer, np.int64, np.int32)) else v
        #             for k, v in rec.items()}
        #         for rec in result.recommendations
        #     ]
        # }
        
        # return jsonify({
        #     'cluster_info': {
        #         'id': result.cluster_id,
        #         'name': result.cluster_name,
        #         'price_range': result.price_range
        #     },
        #     'recommendations': [
        #         {k: float(v) if isinstance(v, (np.floating, np.float64, np.float32)) else
        #             int(v) if isinstance(v, (np.integer, np.int64, np.int32)) else v
        #             for k, v in rec.items()}
        #         for rec in result.recommendations
        #     ]
        # })
        # return jsonify(response)
        # for item in result.recommendations:
        #     for key, value in item.items():
        #         print(f"Key: {key}, Type: {type(value)}")
        # print("523", flush=True)
        # print(f"Type of result.cluster_id: {type(result.cluster_id)}")
        # print(f"Type of result.cluster_name: {type(result.cluster_name)}")
        # print(f"Type of result.price_range: {type(result.price_range)}")
        # print("524", flush=True)
        # for key, value in result.price_range.items():
        #     print(f"Price Range Key: {key}, Type: {type(value)}")
        # print("525", flush=True)
        #######################################
        response = {
            'cluster_info': {
                'id': int(result.cluster_id),
                'name': result.cluster_name,
                'price_range': {
                    'min': float(result.price_range['min']),
                    'max': float(result.price_range['max'])
                }
            },
            'recommendations': [
                {k: float(v) if isinstance(v, (np.floating, np.float64, np.float32)) else
                    int(v) if isinstance(v, (np.integer, np.int64, np.int32)) else v
                    for k, v in rec.items()}
                for rec in result.recommendations
            ]
        }
        return jsonify(response)
        # return jsonify({
        #     'cluster_info': {
        #         'id': result.cluster_id,
        #         'name': result.cluster_name,
        #         'price_range': result.price_range
        #     },
        #     'recommendations': result.recommendations
        # })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['POST'])
def save_feedback():
    """Save user feedback"""
    if not request.is_json:
        print("Request is not JSON format", flush=True)  # Debug log
        return jsonify({
            'error': 'Content-Type must be application/json'
        }), 400
    
    data = request.json
    print("11", flush=True)
    print(data, flush=True)
    try:
        feedback_handler.save_feedback(
            # data.get('image_name'),
            data.get('rating'),
            data.get('feedback')
        )
        return jsonify({'message': 'Feedback saved successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
