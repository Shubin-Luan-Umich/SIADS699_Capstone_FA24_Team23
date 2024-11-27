import mediapipe as mp
import cv2
import numpy as np
import pandas as pd
from typing import Dict, List, Optional
from dataclasses import dataclass
import pickle
import base64
from PIL import Image
from io import BytesIO
from models import ColorAnalyzer

@dataclass
class RecommendationResult:
    """Data class for recommendation results"""
    cluster_id: int
    cluster_name: str
    price_range: Dict[str, float]
    recommendations: List[Dict]


def load_analyzer(file_path: str = 'data/sephora_lipstick_clustering_model.pkl') -> ColorAnalyzer:
    """Load a pre-trained color analyzer with custom Unpickler."""
    class CustomUnpickler(pickle.Unpickler):
        def find_class(self, module, name):
            if name == 'ColorAnalyzer':
                return ColorAnalyzer
            return super().find_class(module, name)

    with open(file_path, 'rb') as f:
        return CustomUnpickler(f).load()

class LipstickRecommender:
    """Lipstick recommendation system based on facial analysis"""
    
    CLUSTER_NAMES = {
        0: 'Warm Brown',
        1: 'Soft Pink',
        2: 'Nude',
        3: 'Classic Red',
        4: 'Deep Burgundy',
        5: 'Coral Pink'
    }
    
    def __init__(self):
        """Initialize the recommender with data and models"""
        # Load product data
        self.df = pd.read_csv('data/lipstick_recommendation_dataset.csv')
        
        # Load KMeans model
        self.analyzer = load_analyzer('models/sephora_lipstick_clustering_model.pkl')
        self.kmeans_model = self.analyzer.kmeans_model
            
        # Initialize MediaPipe
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=True,
            max_num_faces=1,
            min_detection_confidence=0.5
        )
        
        # Process price data
        self._process_price_data()
    
    def _process_price_data(self) -> None:
        """Process price strings to numeric values"""
        self.df['price_value'] = self.df['currentSku.listPrice'].str.replace('$', '').astype(float)
        
        # Calculate price ranges per cluster
        self.price_ranges = {}
        for cluster in self.CLUSTER_NAMES.keys():
            cluster_data = self.df[self.df['color_cluster'] == cluster]
            self.price_ranges[cluster] = {
                'min': float(cluster_data['price_value'].min()),
                'max': float(cluster_data['price_value'].max())
            }
    
    def analyze_skin_tone(self, image: np.ndarray) -> Optional[np.ndarray]:
        """Extract skin tone from facial image"""
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(image_rgb)
        
        if not results.multi_face_landmarks:
            return None
            
        height, width = image.shape[:2]
        landmarks = results.multi_face_landmarks[0]
        
        # Sample cheek points for skin tone
        CHEEK_POINTS = [117, 123, 346, 352]
        colors = []
        
        for point_idx in CHEEK_POINTS:
            x = int(landmarks.landmark[point_idx].x * width)
            y = int(landmarks.landmark[point_idx].y * height)
            
            roi = image_rgb[max(0, y-5):min(height, y+5),
                          max(0, x-5):min(width, x+5)]
            if roi.size > 0:
                color = np.mean(roi, axis=(0,1))
                colors.append(color)
                
        return np.mean(colors, axis=0).astype(int)
    
    def get_recommendations(
        self,
        image: np.ndarray,
        sort_by: str = 'color_similarity',
        n_recommendations: int = 10,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None
    ) -> RecommendationResult:
        """Get lipstick recommendations based on image and filters"""
        # Get skin tone
        skin_rgb = self.analyze_skin_tone(image)
        if skin_rgb is None:
            raise ValueError("No face detected in image")
            
        # Find color cluster
        normalized_rgb = skin_rgb / 255.0
        cluster_id = self.kmeans_model.predict([normalized_rgb])[0]
        
        # Filter products by cluster
        cluster_df = self.df[self.df['color_cluster'] == cluster_id].copy()
        
        # Apply price filter if specified
        if min_price is not None and max_price is not None:
            cluster_df = cluster_df[
                (cluster_df['price_value'] >= min_price) &
                (cluster_df['price_value'] <= max_price)
            ]
        
        # Calculate color similarity if needed
        if sort_by == 'color_similarity':
            cluster_df['color_similarity'] = cluster_df['rgb_value'].apply(
                lambda x: 100 - (np.linalg.norm(np.array(eval(x)) - skin_rgb) / 4.42)
            )
        
        # Sort based on criterion
        sort_criteria = {
            'color_similarity': 'color_similarity',
            'recommendation_score': 'recommendation_score',
            'reviews': 'reviews',
            'rating': 'Rating',
            'price': 'price_value'
        }
        
        sort_ascending = sort_by == 'price'
        sorted_df = cluster_df.sort_values(
            sort_criteria[sort_by],
            ascending=sort_ascending
        ).head(n_recommendations)
        
        # Convert to list of dicts for JSON serialization
        recommendations = sorted_df[[
            'skuID', 'brandName', 'displayName', 'color_description',
            'price_value', 'Rating', 'reviews', 'recommendation_score',
            'lipstick_image_base64'
        ]].to_dict('records')
        
        return RecommendationResult(
            cluster_id=cluster_id,
            cluster_name=self.CLUSTER_NAMES[cluster_id],
            price_range=self.price_ranges[cluster_id],
            recommendations=recommendations
        )
