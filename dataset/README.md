# Sephora Lipstick Recommendation Dataset

## Overview
This dataset provides a curated collection of lipstick recommendations from Sephora, featuring comprehensive product information, color analysis, and user feedback. The data is processed and structured to support color-based product recommendations and analysis.

## Table of Contents
- [Dataset Description](#dataset-description)
- [Data Schema](#data-schema)
- [Color Analysis](#color-analysis)
- [Recommendation System](#recommendation-system)
- [Data Processing](#data-processing)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Dataset Description

### Quick Facts
- **Source**: Sephora.com product data and user reviews
- **Format**: CSV
- **Size**: ~600 records (top 100 products × 6 color clusters)
- **Features**: Product details, color analysis, user ratings, images
- **Use Case**: Color-based lipstick recommendation system

## Data Schema

| Field Name | Type | Description | Example |
|------------|------|-------------|----------|
| `skuID` | string | Unique product identifier | "2036408" |
| `brandName` | string | Cosmetics brand name | "Anastasia Beverly Hills" |
| `displayName` | string | Product display name | "Liquid Lipstick" |
| `color_description` | string | Color description | "American Doll classic blue red" |
| `color_cluster` | integer | Color group (0-5) | 3 |
| `rgb_value` | string | RGB color value | "rgb(149,19,44)" |
| `Rating` | float | User rating (1-5) | 4.5 |
| `reviews` | integer | Number of user reviews | 1250 |
| `currentSku.listPrice` | string | Product price | "$20.00" |
| `full_url` | string | Product URL | "https://www.sephora.com/..." |
| `cover_image_base64` | string | Base64 encoded cover image | (base64 string) |
| `lipstick_image_base64` | string | Base64 encoded color image | (base64 string) |
| `recommendation_score` | float | Overall score (0-100) | 85.67 |

## Color Analysis

### Color Clusters
```python
CLUSTER_NAMES = {
    0: 'Warm Brown',
    1: 'Soft Pink',
    2: 'Nude',
    3: 'Classic Red',
    4: 'Deep Burgundy',
    5: 'Coral Pink'
}
```

### Clustering Methodology
- Algorithm: K-means clustering
- Features: RGB color values
- Optimization: Silhouette score and elbow method
- Validation: Cross-validation across multiple metrics

## Recommendation System

### Score Calculation
The recommendation score (0-100) combines user ratings and review counts:

```python
def calculate_recommendation_score(rating, reviews, max_reviews):
    # Rating component (70% weight)
    rating_score = rating / 5.0
    
    # Review component (30% weight)
    review_score = np.log1p(reviews) / np.log1p(max_reviews)
    
    # Final score
    final_score = (0.7 * rating_score + 0.3 * review_score) * 100
    return round(final_score, 2)
```

### Selection Criteria
- Minimum rating threshold: 4.0
- Required fields: Complete product information and valid images
- Top products: 100 highest scoring products per color cluster

## Data Processing

### Pipeline Steps
1. Data collection from Sephora
2. Color extraction and analysis
3. Cluster assignment
4. Score calculation
5. Quality filtering
6. Top product selection

### Quality Assurance
- Image validation
- Data type verification
- Missing value handling
- Duplicate removal
- Score validation

## Usage

### Loading the Data
```python
import pandas as pd

# Load dataset
df = pd.read_csv('dataset/lipstick_recommendation_dataset.csv')

# Access images
import base64
from io import BytesIO
from PIL import Image

def display_image(base64_str):
    img_data = base64.b64decode(base64_str)
    img = Image.open(BytesIO(img_data))
    return img
```

### Basic Analysis
```python
# Get top products per cluster
top_products = df.groupby('color_cluster').apply(
    lambda x: x.nlargest(10, 'recommendation_score')
)

# Color distribution
color_dist = df['color_cluster'].value_counts()
```

## Contributing
Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and contribute to the project.

## License
This dataset is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

## Acknowledgments
- Sephora for the original product data
- Contributors to the data processing pipeline
- Open source community for tools and libraries

## Contact
For questions and feedback, please open an issue or contact [maintainer email].

---
**Note**: This dataset is intended for research and educational purposes. Please review Sephora's terms of service before using the data commercially.