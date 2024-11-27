import React, { useState } from 'react';
import { styled } from '@mui/material/styles';
import {
  Box,
  Card,
  Grid,
  Slider,
  Typography,
  IconButton,
  MenuItem,
  Select,
  FormControl,
  InputLabel,
} from '@mui/material';
import { AnimatePresence, motion } from 'framer-motion';
import SortIcon from '@mui/icons-material/Sort';
import LocalOfferIcon from '@mui/icons-material/LocalOffer';

// Styled components
const ProductCard = styled(motion(Card))(({ theme }) => ({
  padding: theme.spacing(2),
  position: 'relative',
  transition: 'all 0.3s ease',
  '&:hover': {
    transform: 'translateY(-5px)',
    boxShadow: theme.shadows[8],
  },
}));

const ColorCircle = styled(Box)(({ color }) => ({
  width: '24px',
  height: '24px',
  borderRadius: '50%',
  backgroundColor: color,
  border: '2px solid white',
  boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
  position: 'absolute',
  top: '10px',
  right: '10px',
  zIndex: 2,
}));

const ProductImage = styled('img')({
  width: '100%',
  height: 'auto',
  borderRadius: '8px',
});

const RecommendationView = ({ recommendations, clusterInfo, onFilterChange }) => {
  const [sortBy, setSortBy] = useState('color_similarity');
  const [priceRange, setPriceRange] = useState([
    clusterInfo.price_range.min,
    clusterInfo.price_range.max,
  ]);
  const [numResults, setNumResults] = useState(10);

  // Handle sort change
  const handleSortChange = (event) => {
    setSortBy(event.target.value);
    onFilterChange({
      sortBy: event.target.value,
      priceRange,
      numResults,
    });
  };

  // Handle price range change
  const handlePriceChange = (event, newValue) => {
    setPriceRange(newValue);
    onFilterChange({
      sortBy,
      priceRange: newValue,
      numResults,
    });
  };

  // Handle number of results change
  const handleNumResultsChange = (event) => {
    setNumResults(event.target.value);
    onFilterChange({
      sortBy,
      priceRange,
      numResults: event.target.value,
    });
  };

  return (
    <Box sx={{ p: 3 }}>
      {/* Cluster Information */}
      <Typography variant="h4" gutterBottom>
        {clusterInfo.name} Collection
      </Typography>

      {/* Filter Controls */}
      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid item xs={12} md={4}>
          <FormControl fullWidth>
            <InputLabel>Sort By</InputLabel>
            <Select
              value={sortBy}
              onChange={handleSortChange}
              startAdornment={<SortIcon />}
            >
              <MenuItem value="color_similarity">Color Match</MenuItem>
              <MenuItem value="recommendation_score">Recommendation Score</MenuItem>
              <MenuItem value="reviews">Number of Reviews</MenuItem>
              <MenuItem value="rating">Rating</MenuItem>
              <MenuItem value="price">Price</MenuItem>
            </Select>
          </FormControl>
        </Grid>

        <Grid item xs={12} md={4}>
          <Typography gutterBottom>Price Range</Typography>
          <Slider
            value={priceRange}
            onChange={handlePriceChange}
            valueLabelDisplay="auto"
            min={clusterInfo.price_range.min}
            max={clusterInfo.price_range.max}
            marks
          />
        </Grid>

        <Grid item xs={12} md={4}>
          <FormControl fullWidth>
            <InputLabel>Number of Results</InputLabel>
            <Select value={numResults} onChange={handleNumResultsChange}>
              <MenuItem value={5}>5 Products</MenuItem>
              <MenuItem value={10}>10 Products</MenuItem>
              <MenuItem value={15}>15 Products</MenuItem>
              <MenuItem value={20}>20 Products</MenuItem>
            </Select>
          </FormControl>
        </Grid>
      </Grid>

      {/* Product Grid */}
      <AnimatePresence>
        <Grid container spacing={3}>
          {recommendations.map((product, index) => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={product.skuID}>
              <ProductCard
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
              >
                {/* Product Color Circle */}
                <ColorCircle color={product.rgb_value} />

                {/* Product Image */}
                <ProductImage
                  src={`data:image/jpeg;base64,${product.cover_image_base64}`}
                  alt={product.displayName}
                />

                {/* Product Info */}
                <Box sx={{ mt: 2 }}>
                  <Typography variant="h6" noWrap>
                    {product.brandName}
                  </Typography>
                  <Typography variant="subtitle1" noWrap>
                    {product.displayName}
                  </Typography>
                  <Typography variant="body2" color="text.secondary" noWrap>
                    {product.color_description}
                  </Typography>

                  <Box sx={{ mt: 1, display: 'flex', alignItems: 'center', gap: 1 }}>
                    <LocalOfferIcon color="primary" />
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
      </AnimatePresence>
    </Box>
  );
};

export default RecommendationView;
