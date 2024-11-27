import React, { useState } from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import {
  CssBaseline,
  Container,
  AppBar,
  Toolbar,
  Typography,
  Alert,
  Snackbar,
} from '@mui/material';
import axios from 'axios';

import ImageUpload from './components/ImageUpload';
import RecommendationView from './components/RecommendationView';

// Create theme
const theme = createTheme({
  palette: {
    primary: {
      main: '#FF4081', // Pink shade
    },
    secondary: {
      main: '#FF80AB', // Light pink
    },
    background: {
      default: '#fafafa',
    },
  },
  typography: {
    fontFamily: '"Helvetica Neue", Arial, sans-serif',
    h4: {
      fontWeight: 600,
    },
  },
  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 12,
        },
      },
    },
  },
});

function App() {
  const [recommendations, setRecommendations] = useState(null);
  const [clusterInfo, setClusterInfo] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleImageUpload = async (file) => {
    setIsLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('image', file);

    try {
      const response = await axios.post('http://localhost:5001/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      setClusterInfo(response.data.cluster_info);
      setRecommendations(response.data.recommendations);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  const handleFilterChange = async ({ sortBy, priceRange, numResults }) => {
    setIsLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('sort_by', sortBy);
    formData.append('n_recommendations', numResults);
    formData.append('min_price', priceRange[0]);
    formData.append('max_price', priceRange[1]);

    try {
      const response = await axios.post(
        'http://localhost:5001/recommendations',
        formData
      );

      setRecommendations(response.data.recommendations);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      
      {/* App Bar */}
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6" component="div">
            LipShade Lab 💄
          </Typography>
        </Toolbar>
      </AppBar>

      <Container maxWidth="lg" sx={{ py: 4 }}>
        {/* Image Upload */}
        <ImageUpload 
          onImageUpload={handleImageUpload}
          isLoading={isLoading}
        />

        {/* Recommendations */}
        {recommendations && clusterInfo && (
          <RecommendationView
            recommendations={recommendations}
            clusterInfo={clusterInfo}
            onFilterChange={handleFilterChange}
          />
        )}

        {/* Error Snackbar */}
        <Snackbar
          open={!!error}
          autoHideDuration={6000}
          onClose={() => setError(null)}
        >
          <Alert severity="error" onClose={() => setError(null)}>
            {error}
          </Alert>
        </Snackbar>
      </Container>
    </ThemeProvider>
  );
}

export default App;
