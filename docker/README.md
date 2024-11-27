# LipShade Lab - Personalized Lipstick Recommendation System

LipShade Lab is an AI-powered web application that provides personalized lipstick recommendations based on user's skin tone analysis. The system uses facial detection, color analysis, and a sophisticated recommendation engine to suggest the most suitable lipstick products.

## Project Structure

```
lipshade-lab/
├── frontend/                  # Frontend React application
│   ├── public/
│   │   └── index.html        # HTML template
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── ImageUpload.js          # Image upload interface
│   │   │   └── RecommendationView.js   # Product recommendations display
│   │   ├── App.js           # Main application component
│   │   └── index.js         # Application entry point
│   ├── Dockerfile           # Frontend container configuration
│   └── package.json         # Frontend dependencies
│
├── backend/                  # Backend Flask server
│   ├── data/                # Data directory
│   │   └── chromatic_recommendation_dataset.csv  # Product database
│   ├── models/              # Model directory
│   │   └── sephora_lipstick_clustering_model.pkl # Trained clustering model
│   ├── app.py              # Main Flask application
│   ├── lipstick_recommender.py  # Recommendation engine
│   ├── image_processor.py   # Image processing utilities
│   ├── feedback_handler.py  # User feedback management
│   ├── Dockerfile          # Backend container configuration
│   └── requirements.txt     # Python dependencies
│
├── mysql/                   # MySQL database
│   └── init.sql            # Database initialization script
│
├── docker-compose.yml       # Container orchestration
└── README.md               # Project documentation
```

## Key Components

### Frontend Components

1. **ImageUpload.js**
   - Handles image upload through drag-and-drop or file selection
   - Provides real-time upload feedback
   - Validates image format and size

2. **RecommendationView.js**
   - Displays product recommendations in a grid layout
   - Implements filtering and sorting functionality
   - Shows product details with color swatches
   - Handles price range selection

3. **App.js**
   - Manages application state
   - Coordinates communication with backend
   - Implements global theme and styling

### Backend Services

1. **app.py**
   - Main Flask application
   - Handles HTTP requests
   - Manages API endpoints
   - Coordinates various services

2. **lipstick_recommender.py**
   - Implements recommendation logic
   - Processes skin tone analysis
   - Manages product filtering and sorting
   - Handles color matching algorithms

3. **image_processor.py**
   - Processes uploaded images
   - Implements facial detection
   - Extracts skin tone information
   - Handles image validation

4. **feedback_handler.py**
   - Manages user feedback
   - Handles database interactions
   - Stores user ratings and comments

### Database

- MySQL database for storing:
  - User feedback
  - Usage analytics
  - System performance metrics

## Technologies Used

### Frontend
- React.js
- Material-UI
- Framer Motion (animations)
- Axios (HTTP client)
- React Dropzone

### Backend
- Flask
- OpenCV
- MediaPipe (facial detection)
- Pandas (data processing)
- scikit-learn (clustering)
- MySQL Connector

### Infrastructure
- Docker
- Docker Compose
- MySQL

## Setup and Installation

1. **Prerequisites**
   ```bash
   - Docker
   - Docker Compose
   ```

2. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/lipshade-lab.git
   cd lipshade-lab
   ```

3. **Start Application**
   ```bash
   # Clean up old containers and images
   docker-compose down
   docker system prune -f

   # Rebuild and start containers
   docker-compose up --build
   ```

4. **Access Application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5001

## API Endpoints

### Image Upload
```
POST /upload
- Accepts multipart/form-data with image file
- Returns initial recommendations and cluster information
```

### Recommendations
```
POST /recommendations
- Accepts filter parameters (sort_by, price_range, etc.)
- Returns filtered product recommendations
```

### Feedback
```
POST /feedback
- Accepts user feedback and ratings
- Stores feedback in database
```

## Configuration

1. **Environment Variables**
   - Create `.env` file in root directory
   - Set required environment variables:
     ```
     MYSQL_ROOT_PASSWORD=rootpassword
     MYSQL_DATABASE=lipshadelab
     MYSQL_USER=lipshadeuser
     MYSQL_PASSWORD=lipshadepass
     ```

2. **Docker Configuration**
   - Adjust docker-compose.yml for custom requirements
   - Modify container specifications as needed

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Sephora for product data
- MediaPipe team for facial detection
- Material-UI for component library
