import mysql.connector
from datetime import datetime
from typing import List, Dict, Optional

class FeedbackHandler:
    """Handles user feedback storage and retrieval for the lipstick recommendation system."""
    
    def __init__(self):
        """Initialize database configuration."""
        self.db_config = {
            'host': 'mysql',
            'user': 'lipshadeuser',
            'password': 'lipshadepass',
            'database': 'lipshadelab'
        }

    def init_db(self) -> None:
        """Initialize database tables.
        
        Creates necessary tables if they don't exist.
        """
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            
            # Create feedback table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS feedback (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    image_name VARCHAR(255),
                    cluster_id INT,
                    rating INT CHECK (rating >= 1 AND rating <= 5),
                    feedback_text TEXT,
                    selected_products TEXT,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    user_agent VARCHAR(255),
                    ip_address VARCHAR(45)
                )
            ''')
            
            # Create recommendations_feedback table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS recommendations_feedback (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    feedback_id INT,
                    product_id VARCHAR(50),
                    is_helpful BOOLEAN,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (feedback_id) REFERENCES feedback(id)
                )
            ''')
            
            conn.commit()
            
        except Exception as e:
            print(f"Database initialization error: {str(e)}")
            raise
            
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def save_feedback(self, 
                     rating: int,
                     feedback_text: str,
                     ip_address: Optional[str] = None) -> int:
        """Save user feedback to database.
        Args:
            rating: User rating (1-5)
            feedback_text: User feedback text
            ip_address: User's IP address
        Returns:
            int: ID of the inserted feedback

        Raises:
            ValueError: If rating is invalid
            Exception: If database operation fails
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            query = '''
                INSERT INTO feedback (
                    rating, feedback_text
                ) VALUES (%s, %s)
            '''
            values = (
                rating,
                feedback_text

            )
            cursor.execute(query, values)
            conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error saving feedback: {str(e)}")
            raise
        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def get_all_feedback(self) -> List[Dict]:
        """Retrieve all feedback from database.

        Returns:
            List[Dict]: List of feedback entries
        """
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor(dictionary=True)

            cursor.execute('''
                SELECT
                    f.*,
                    COUNT(rf.id) as recommendation_responses,
                    SUM(rf.is_helpful) as helpful_count
                FROM feedback f
                LEFT JOIN recommendations_feedback rf ON f.id = rf.feedback_id
                GROUP BY f.id
                ORDER BY f.created_at DESC
            ''')

            feedback_list = cursor.fetchall()

            # Convert datetime objects to string for JSON serialization
            for feedback in feedback_list:
                feedback['created_at'] = feedback['created_at'].isoformat()
                if feedback['selected_products']:
                    feedback['selected_products'] = \
                        feedback['selected_products'].split(',')

            return feedback_list

        except Exception as e:
            print(f"Error retrieving feedback: {str(e)}")
            raise

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def add_recommendation_feedback(self,
                                  feedback_id: int,
                                  product_id: str,
                                  is_helpful: bool) -> None:
        """Add feedback for specific product recommendations.

        Args:
            feedback_id: ID of the original feedback
            product_id: ID of the recommended product
            is_helpful: Whether the recommendation was helpful
        """
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()

            query = '''
                INSERT INTO recommendations_feedback (
                    feedback_id, product_id, is_helpful
                ) VALUES (%s, %s, %s)
            '''

            values = (feedback_id, product_id, is_helpful)

            cursor.execute(query, values)
            conn.commit()

        except Exception as e:
            print(f"Error adding recommendation feedback: {str(e)}")
            raise

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()
