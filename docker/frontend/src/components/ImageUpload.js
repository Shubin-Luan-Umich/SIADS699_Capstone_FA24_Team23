import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import { styled } from '@mui/material/styles';
import {
  Box,
  Paper,
  Typography,
  CircularProgress,
} from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { motion } from 'framer-motion';

const UploadZone = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  textAlign: 'center',
  cursor: 'pointer',
  border: `2px dashed ${theme.palette.primary.main}`,
  backgroundColor: theme.palette.background.default,
  transition: 'all 0.3s ease',
  '&:hover': {
    backgroundColor: theme.palette.action.hover,
  },
}));

const PreviewImage = styled('img')({
  maxWidth: '100%',
  maxHeight: '400px',
  borderRadius: '8px',
  boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
});

const ImageUpload = ({ onImageUpload, isLoading }) => {
  const onDrop = useCallback((acceptedFiles) => {
    onImageUpload(acceptedFiles[0]);
  }, [onImageUpload]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: 'image/*',
    multiple: false,
  });

  return (
    <Box sx={{ mb: 4 }}>
      <UploadZone
        component={motion.div}
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        {...getRootProps()}
      >
        <input {...getInputProps()} />
        <CloudUploadIcon sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
        <Typography variant="h6" gutterBottom>
          {isDragActive
            ? "Drop your photo here!"
            : "Drag & drop your photo here or click to select"}
        </Typography>
        <Typography variant="body2" color="text.secondary">
          We'll analyze your skin tone and find the perfect lipstick matches
        </Typography>
        {isLoading && (
          <CircularProgress 
            sx={{ mt: 2 }} 
            size={24} 
            thickness={4} 
          />
        )}
      </UploadZone>
    </Box>
  );
};

export default ImageUpload;
