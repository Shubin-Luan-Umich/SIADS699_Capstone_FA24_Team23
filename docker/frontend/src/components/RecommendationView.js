import React, { useState, useContext } from 'react';
import { styled } from '@mui/material/styles';
import FeedbackDialog from './FeedbackDialog';
import {
  Box,
  Button,
  Card,
  Grid,
  Slider,
  Typography,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Link,
} from '@mui/material';
import { motion } from 'framer-motion';
import axios from 'axios';
import { ImageContext } from '../contexts/ImageContext';

const ProductCard = styled(motion(Card))(({ theme }) => ({
  padding: theme.spacing(2),
  position: 'relative',
  transition: 'all 0.3s ease',
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
  '&:hover': {
    transform: 'translateY(-5px)',
    boxShadow: theme.shadows[8],
  },
}));

const ProductImage = styled('img')({
  width: '100%',
  height: 300,
  borderRadius: '8px',
  objectFit: 'cover',
});

const ColorCircle = styled(Box)({
  width: '24px',
  height: '24px',
  borderRadius: '50%',
  border: '2px solid white',
  boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
  position: 'absolute',
  top: '10px',
  right: '10px',
  zIndex: 2,
  overflow: 'hidden',
});

const PriceRangeSlider = styled(Slider)(({ theme }) => ({
  width: '100%',
  marginTop: theme.spacing(2),
}));


const RecommendationView = ({ recommendations, clusterInfo, onFilterChange }) => {
  // const [sortBy, setSortBy] = useState('color_similarity');
  const [sortBy, setSortBy] = useState('recommendation_score');
  const [priceRange, setPriceRange] = useState([
    clusterInfo.price_range.min,
    clusterInfo.price_range.max
  ]);
  const [numResults, setNumResults] = useState(10);

  const [feedbackOpen, setFeedbackOpen] = useState(false);
  const { imageFile } = useContext(ImageContext);

  const uniqueRecommendations = recommendations.filter((item, index, self) =>
    index === self.findIndex((t) => t.skuID === item.skuID)
  );

  const handleSortChange = (event) => {
    setSortBy(event.target.value);
    onFilterChange({ sortBy: event.target.value, priceRange, numResults });
  };

  const handlePriceChange = (event, newValue) => {
    setPriceRange(newValue);
    onFilterChange({ sortBy, priceRange: newValue, numResults });
  };

  const handleNumResultsChange = (event) => {
    setNumResults(event.target.value);
    onFilterChange({ sortBy, priceRange, numResults: event.target.value });
  };

  const handleFeedbackSubmit = async (feedbackData) => {
    try {
      await axios.post('http://localhost:5001/feedback', {
        image_name: imageFile?.name,
        rating: feedbackData.rating,
        feedback: feedbackData.feedback
      }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      alert('Thank you for your feedback!');
    } catch (error) {
      console.error('Error submitting feedback:', error);
      alert('Failed to submit feedback. Please try again.');
    }
  };

  const FeedbackButton = styled(Button)(({ theme }) => ({
    position: 'fixed',
    right: theme.spacing(3),
    bottom: theme.spacing(3),
    zIndex: 1000,
  }));

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        {clusterInfo.name} Collection
      </Typography>

      <Grid item xs={12} sm={6} md={3} sx={{ height: '100%' }}>
        <Grid item xs={12} md={4}>
          <FormControl fullWidth sx={{ minWidth: 200 }}>
            <InputLabel id="sort-label">Sort By</InputLabel>
            <Select
              labelId="sort-label"
              value={sortBy}
              onChange={handleSortChange}
              label="Sort By"
              sx={{ height: 40 }}
            >
              {/* <MenuItem value="color_similarity">Color Match</MenuItem> */}
              <MenuItem value="recommendation_score">Recommendation Score</MenuItem>
              <MenuItem value="reviews">Number of Reviews</MenuItem>
              <MenuItem value="rating">Rating</MenuItem>
              <MenuItem value="price">Price</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        <Grid item xs={12} md={4}>
          <Box sx={{ width: '100%', px: 2 }}>
            <Typography gutterBottom>
              Price Range: ${priceRange[0]} - ${priceRange[1]}
            </Typography>
            <PriceRangeSlider
              value={priceRange}
              onChange={handlePriceChange}
              valueLabelDisplay="auto"
              min={clusterInfo.price_range.min}
              max={clusterInfo.price_range.max}
              marks={[
                { value: clusterInfo.price_range.min, label: `$${clusterInfo.price_range.min}` },
                { value: clusterInfo.price_range.max, label: `$${clusterInfo.price_range.max}` }
              ]}
            />
          </Box>
        </Grid>

        <Grid item xs={12} md={4}>
          <FormControl fullWidth sx={{ minWidth: 150 }}>
            <InputLabel id="results-label">Number of Results</InputLabel>
            <Select
              labelId="results-label"
              value={numResults}
              onChange={handleNumResultsChange}
              label="Number of Results"
              sx={{ height: 40 }}
            >
              <MenuItem value={5}>5 Products</MenuItem>
              <MenuItem value={10}>10 Products</MenuItem>
              <MenuItem value={15}>15 Products</MenuItem>
              <MenuItem value={20}>20 Products</MenuItem>
            </Select>
          </FormControl>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        {uniqueRecommendations.slice(0, numResults).map((product, index) => (
          <Grid item xs={12} sm={6} md={3} key={product.skuID}>
            <ProductCard
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
            >
              <ColorCircle sx={{ backgroundColor: product.rgb_value }}>
                {product.cover_image_base64 && (
                  <Box
                    component="img"
                    src={`data:image/jpeg;base64,${product.lipstick_image_base64}`}
                    sx={{
                      width: '100%',
                      height: '100%',
                      objectFit: 'cover',
                      opacity: 0.7,
                    }}
                  />
                )}
              </ColorCircle>
              <Link 
                href={product.full_url} 
                target="_blank" 
                rel="noopener noreferrer"
                sx={{ 
                  display: 'block',
                  '&:hover': {
                    opacity: 0.9,
                  }
                }}
              >
                <ProductImage
                  src={`data:image/jpeg;base64,${product.cover_image_base64}`}
                  alt={product.displayName}
                />
              </Link>
              <Box sx={{ mt: 2 }}>
                <Typography variant="h6" noWrap>
                  {product.brandName}
                </Typography>
                <Typography 
                  variant="subtitle1" 
                  noWrap 
                  component="a"
                  href={product.full_url}
                  target="_blank"
                  sx={{
                    color: 'primary.main',
                    textDecoration: 'none',
                    '&:hover': {
                      textDecoration: 'underline',
                    },
                  }}
                >
                  {product.displayName}
                </Typography>
                <Typography variant="body2" color="text.secondary" noWrap>
                  {product.color_description}
                </Typography>

                <Box sx={{ mt: 1, display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Typography variant="h6" color="primary">
                    ${product.price_value}
                  </Typography>
                </Box>

                <Box sx={{ mt: 1 }}>
                  <Typography variant="body2">
                    ★ {product.Rating.toFixed(1)} ({product.reviews} reviews)
                  </Typography>
                </Box>
              </Box>
            </ProductCard>
          </Grid>
        ))}
      </Grid>
      <FeedbackButton
        variant="contained"
        color="primary"
        onClick={() => setFeedbackOpen(true)}
      >
        Give Feedback
      </FeedbackButton>

      <FeedbackDialog
        open={feedbackOpen}
        onClose={() => setFeedbackOpen(false)}
        onSubmit={handleFeedbackSubmit}
      />
    </Box>
  );
};

export default RecommendationView;