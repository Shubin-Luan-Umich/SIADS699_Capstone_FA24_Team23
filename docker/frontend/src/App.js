import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [imageInfo, setImageInfo] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [rating, setRating] = useState(5);
  const [hoveredRating, setHoveredRating] = useState(null);
  const [feedback, setFeedback] = useState('');
  const [showFeedback, setShowFeedback] = useState(false);
  const [error, setError] = useState(null);

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setError(null);

    // Create image preview	
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagePreview(reader.result);
      };
      reader.readAsDataURL(file);
    } else {
      setImagePreview(null);
    }

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post('http://localhost:5001/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setImageInfo(response.data);
      setShowFeedback(true);
    } catch (error) {
      console.error('Error:', error);
      setError('Failed to upload image. Please try again.');
    }
  };

  const submitFeedback = async () => {
    try {
      await axios.post('http://localhost:5001/feedback', {
        image_name: selectedFile?.name,
        rating: rating,
        feedback: feedback
      });
      alert('Thank you for your feedback!');
      setSelectedFile(null);
      setImageInfo(null);
      setImagePreview(null);
      setRating(5);
      setFeedback('');
      setShowFeedback(false);
      setError(null);
    } catch (error) {
      console.error('Error:', error);
      setError('Failed to submit feedback. Please try again.');
    }
  };

  // Star Rating Component
  const StarRating = () => {
    return (
      <div style={{ fontSize: '30px' }}>
        {[1, 2, 3, 4, 5].map((star) => (
          <span
            key={star}
            onMouseEnter={() => setHoveredRating(star)}
            onMouseLeave={() => setHoveredRating(null)}
            onClick={() => setRating(star)}
            style={{
              cursor: 'pointer',
              color: (hoveredRating || rating) >= star ? '#FFD700' : '#D3D3D3',
              marginRight: '5px'
            }}
          >
            ★
          </span>
        ))}
      </div>
    );
  };

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <h1>LipShade Lab</h1>

      {/* Image Upload Section */}
      <div style={{ marginBottom: '20px' }}>
        <input
          type="file"
          onChange={handleFileUpload}
          accept="image/*"
          style={{ marginBottom: '10px' }}
        />
        {selectedFile && (
          <p>Selected file: {selectedFile.name}</p>
        )}
      </div>

      {/* Error Display */}
      {error && (
        <div style={{ 
          color: 'red', 
          backgroundColor: '#ffe6e6', 
          padding: '10px', 
          borderRadius: '4px',
          marginBottom: '20px'
        }}>
          {error}
        </div>
      )}

      {/* Image Information and Preview Display */}
      {imageInfo && (
        <div style={{ 
          marginBottom: '20px',
          display: 'flex',
          flexDirection: 'column',
          gap: '20px',
          padding: '20px',
          border: '1px solid #ddd',
          borderRadius: '8px',
          backgroundColor: '#f8f9fa'
        }}>
          <h2 style={{ margin: '0 0 15px 0' }}>Image Information:</h2>
          
          <div style={{ 
            display: 'flex', 
            gap: '40px',
            alignItems: 'flex-start'
          }}>
            {/* Image Details */}
            <div style={{ flex: '1' }}>
              <p><strong>Filename:</strong> {imageInfo.filename}</p>
              <p><strong>Extension:</strong> {imageInfo.extension}</p>
              <p><strong>Dimensions:</strong> {imageInfo.width} x {imageInfo.height} pixels</p>
              <p><strong>Size:</strong> {imageInfo.size_kb.toFixed(2)} KB</p>
            </div>

            {/* Image Preview */}
            <div style={{ 
              flex: '1',
              maxWidth: '400px'
            }}>
              {imagePreview && (
                <div style={{ 
                  border: '1px solid #ddd',
                  borderRadius: '4px',
                  padding: '10px',
                  backgroundColor: 'white'
                }}>
                  <img
                    src={imagePreview}
                    alt="Preview"
                    style={{
                      maxWidth: '100%',
                      height: 'auto',
                      display: 'block',
                      margin: '0 auto'
                    }}
                  />
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Feedback Section */}
      {showFeedback && (
        <div style={{ 
          border: '1px solid #ccc', 
          padding: '20px',
          borderRadius: '5px',
          backgroundColor: '#f9f9f9'
        }}>
          <h2>Please Rate Your Experience</h2>

          <div style={{ marginBottom: '15px' }}>
            <p>Satisfaction Rating:</p>
            <StarRating />
            <p style={{ fontSize: '14px', color: '#666', marginTop: '5px' }}>
              Current Rating: {rating} stars
            </p>
          </div>

          <div style={{ marginBottom: '15px' }}>
            <p>Feedback:</p>
            <textarea
              value={feedback}
              onChange={(e) => setFeedback(e.target.value)}
              placeholder="Please enter your feedback..."
              style={{ 
                width: '95%', 
                height: '100px',
                padding: '10px',
                marginBottom: '10px',
                borderRadius: '4px',
                border: '1px solid #ddd'
              }}
            />
          </div>

          <button 
            onClick={submitFeedback}
            style={{
              backgroundColor: '#4CAF50',
              color: 'white',
              padding: '10px 20px',
              border: 'none',
              borderRadius: '4px',
              cursor: 'pointer',
              fontSize: '16px'
            }}
          >
            Submit Feedback
          </button>
        </div>
      )}
    </div>
  );
}


export default App;