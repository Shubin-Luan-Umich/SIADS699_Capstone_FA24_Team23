from flask import Flask, request, jsonify
from flask_cors import CORS
from image_processor import ImageProcessor
from feedback_handler import FeedbackHandler
import traceback

app = Flask(__name__)
CORS(app)

feedback_handler = FeedbackHandler()
feedback_handler.init_db()

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        processor = ImageProcessor()
        image_info = processor.process_image(file)
        return jsonify(image_info)
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

@app.route('/feedback', methods=['POST'])
def save_feedback():
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

@app.route('/feedback/list', methods=['GET'])
def get_feedback():
    try:
        feedback_list = feedback_handler.get_all_feedback()
        return jsonify(feedback_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)