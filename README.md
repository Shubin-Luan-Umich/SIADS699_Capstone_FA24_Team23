> **🚧 UNDER CONSTRUCTION 🚧**
> 
# LipShade Lab 💄

> An AI-powered web application that recommends personalized lipstick colors and brands based on user-uploaded images.

## 🌟 Overview

LipShade Lab is a Docker-based application that leverages image processing and machine learning to provide customized lipstick recommendations. Users can upload photos through an intuitive web interface, receive instant color and brand suggestions, and provide feedback to help improve future recommendations.

## ✨ Key Features

- 🖼️ **Smart Image Upload**: Seamless photo upload experience with instant processing
- 🎨 **Intelligent Color Analysis**: Advanced image processing for accurate color recommendations
- 💄 **Brand Matching**: Matches your perfect shade with available products
- 📊 **User Feedback System**: Collects and analyzes user ratings for continuous improvement
- 🔄 **Containerized Architecture**: Fully dockerized for consistent deployment and scaling

## 🛠️ Tech Stack

- **Frontend**: React.js
- **Backend**: Python Flask
- **Database**: MySQL
- **Containerization**: Docker & Docker Compose

### Key Libraries
- Frontend: Axios, React Router, Material-UI
- Backend: Flask-CORS, Pillow, MySQL Connector/Python

## 🚀 Getting Started

### Prerequisites

- Docker Engine (version 20.10.0 or higher)
- Docker Compose (version 2.0.0 or higher)
- Git

### Installation

1. Clone the repository
```bash
git clone https://github.com/Shubin-Luan-Umich/SIADS699_Capstone_FA24_Team15.git
cd docker
```

2. Launch the application
```bash

   # Clean up old containers and images
   docker-compose down
   docker system prune -f

   # Delete node_modules
   rm -rf frontend/node_modules

   # Rebuild and start containers
   docker-compose up --build

```

3. Access the application at [http://localhost:3000](http://localhost:3000)

## 📱 Usage Guide

### 1. Upload Your Photo
- Click the upload button or drag & drop your photo
- Supported formats: JPG, PNG, HEIC
- Recommended image size: 1024x1024px or larger

### 2. Get Recommendations
- View your processed image
- Receive personalized lipstick color recommendations
- Browse matching product suggestions

### 3. Provide Feedback
- Rate your experience (1-5 stars)
- Share detailed feedback (optional)
- Help improve future recommendations

## 📁 Project Structure

```
lipshade-lab-app/
├── docker-compose.yml          # Container orchestration
├── frontend/
│   ├── Dockerfile             # Frontend container config
│   ├── package.json           # Dependencies
│   └── src/
│       ├── App.js            # Main React component
│       └── index.js          # Entry point
├── backend/
│   ├── Dockerfile            # Backend container config
│   ├── app.py               # Flask application
│   ├── feedback_handler.py   # Feedback management
│   ├── image_processor.py    # Image analysis
│   └── requirements.txt      # Python dependencies
└── README.md                 # Documentation
```

## 🔮 Future Roadmap

- 🔐 **User Authentication**: Personal accounts and history tracking
- 🎨 **Enhanced UI/UX**: More intuitive and responsive design
- 📱 **Mobile App**: Native mobile applications
- 🤖 **Advanced AI**: Improved color detection and matching
- ☁️ **Cloud Deployment**: Scalable cloud infrastructure

## 👥 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## 📬 Contact

For questions or feedback, please contact our team:

- Shubin Luan - shubinl@umich.edu

---
Built with ❤️ by Team 23 | SIADS699 Capstone Project FA24
