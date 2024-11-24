import mysql.connector
from datetime import datetime
import time

class FeedbackHandler:
    def __init__(self):
        self.db_config = {
            'host': 'mysql',
            'user': 'lipshadeuser',
            'password': 'lipshadepass',
            'database': 'lipshadelab'
        }


    def init_db(self):
        max_retries = 10
        retry_delay = 5  # seconds
        retries = 0

        while retries < max_retries:
            try:
                conn = mysql.connector.connect(**self.db_config)
                cursor = conn.cursor()

                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS feedback (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        image_name VARCHAR(255),
                        rating INT,
                        feedback_text TEXT,
                        created_at DATETIME
                    )
                ''')

                conn.commit()
                cursor.close()
                conn.close()
                print("Database initialized successfully.")
                break
            except mysql.connector.Error as err:
                print(f"Database connection failed: {err}")
                retries += 1
                print(f"Retrying ({retries}/{max_retries}) in {retry_delay} seconds...")
                time.sleep(retry_delay)
        else:
            print("Could not connect to the database after several attempts.")
            raise Exception("Database connection failed")

    def save_feedback(self, image_name, rating, feedback_text):
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor()
        
        query = '''
            INSERT INTO feedback (image_name, rating, feedback_text, created_at)
            VALUES (%s, %s, %s, %s)
        '''
        values = (image_name, rating, feedback_text, datetime.now())
        
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_all_feedback(self):
        conn = mysql.connector.connect(**self.db_config)
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute('SELECT * FROM feedback ORDER BY created_at DESC')
        feedback_list = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return feedback_list