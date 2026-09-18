# 🩺 Multi-Disease Prediction System

An AI/ML-powered full-stack web application for predicting the likelihood of multiple diseases using trained machine learning models.

The project combines a modern **React + Vite frontend** with a **FastAPI backend** and machine learning models to provide an interactive disease prediction platform.

> 🚧 **Status: Active Development**
>
> This project is being improved and extended with better UI/UX, backend improvements, validation, machine learning enhancements, and additional AI-powered healthcare features.

---

## 🌟 Overview

The Multi-Disease Prediction System provides a centralized web interface where users can enter relevant medical parameters and receive predictions from trained machine learning models.

### Currently Supported Diseases

- 🩸 Diabetes
- ❤️ Heart Disease
- 🧠 Parkinson's Disease

### Planned

- 🧠 Brain Tumor Detection
- 📷 Medical Image Analysis
- 📊 Prediction History
- 👤 User Authentication
- 🗄️ Database Integration
- 📄 Medical Report Generation

The main objective of this project is to demonstrate how machine learning models can be integrated into a modern full-stack web application.

---

## ✨ Features

### 🩸 Diabetes Prediction

Predicts the likelihood of diabetes using 8 numerical features.

### ❤️ Heart Disease Prediction

Predicts the likelihood of heart disease using 13 numerical features.

### 🧠 Parkinson's Disease Prediction

Predicts the likelihood of Parkinson's disease using 22 numerical features.

### ⚡ FastAPI Backend

REST API built using FastAPI for fast and efficient communication between the frontend and machine learning models.

### ⚛️ React Frontend

Interactive user interface built using React and Vite.

### 🔐 Input Validation

API requests are validated using Pydantic before being passed to the machine learning models.

### 📚 API Documentation

FastAPI automatically provides interactive Swagger and ReDoc documentation.

### 📱 Responsive Interface

The frontend is designed to work across desktop and mobile screen sizes.

---

## 🏗️ System Architecture

    ┌──────────────────────────┐
    │      React + Vite        │
    │        Frontend          │
    └────────────┬─────────────┘
                 │
                 │ REST API
                 ▼
    ┌──────────────────────────┐
    │         FastAPI           │
    │         Backend           │
    └────────────┬─────────────┘
                 │
        ┌────────┼────────┐
        │        │        │
        ▼        ▼        ▼
    ┌───────┐ ┌───────┐ ┌────────────┐
    │Diabetes│ │ Heart │ │ Parkinson's│
    │ Model  │ │ Model │ │   Model    │
    └───────┘ └───────┘ └────────────┘

---

## 🛠️ Tech Stack

### Frontend

- React
- Vite
- JavaScript
- JSX
- HTML5
- CSS3

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- NumPy

### Machine Learning

- Scikit-learn
- Pandas
- NumPy
- Pickle

### Development

- Git
- GitHub
- VS Code
- REST APIs

---

## 📁 Project Structure

    Multi-Disease-Prediction-main/
    │
    ├── backend/
    │   ├── main.py
    │   └── __pycache__/
    │
    ├── datasets/
    │   ├── diabetes.csv
    │   ├── heart.csv
    │   └── parkinsons.csv
    │
    ├── models/
    │   ├── diabetes_model.sav
    │   ├── heart_disease_model.sav
    │   └── parkinsons_model.sav
    │
    ├── frontend/
    │   ├── src/
    │   │   ├── App.jsx
    │   │   ├── diseaseData.js
    │   │   ├── main.jsx
    │   │   └── styles.css
    │   │
    │   ├── index.html
    │   ├── package.json
    │   ├── package-lock.json
    │   └── vite.config.js
    │
    ├── notebook/
    │   ├── Multiple_disease_prediction_system_diabetes.ipynb
    │   ├── Multiple_disease_prediction_system_heart.ipynb
    │   └── Multiple_disease_prediction_system_Parkinsons.ipynb
    │
    ├── README.md
    └── .gitignore

---

# 🚀 Getting Started

Follow the steps below to run the project locally.

---

## 📋 Prerequisites

Make sure you have the following installed:

- Python 3.10+
- Node.js
- npm
- Git

Check your versions:

    python3 --version
    node --version
    npm --version
    git --version

---

# 🐍 Backend Setup

## 1. Clone the Repository

Clone your GitHub repository:

    git clone https://github.com/YOUR-USERNAME/Multi-Disease-Prediction.git

Move into the project:

    cd Multi-Disease-Prediction

---

## 2. Create a Python Virtual Environment

### macOS / Linux

    python3 -m venv .venv

Activate it:

    source .venv/bin/activate

### Windows

    python -m venv .venv

Activate it:

    .venv\Scripts\activate

---

## 3. Install Backend Dependencies

Install the required Python packages:

    pip install -r requirements.txt

If a requirements.txt file is not available yet, install the main dependencies:

    pip install fastapi uvicorn numpy pandas scikit-learn pydantic

---

# ▶️ Run the Backend

From the project root directory, run:

    uvicorn backend.main:app --reload

The backend will normally be available at:

    http://127.0.0.1:8000

You can test the API by opening:

    http://127.0.0.1:8000

Expected response:

    {
      "message": "Multi Disease Prediction API is running"
    }

---

# 📚 API Documentation

FastAPI provides automatic interactive API documentation.

### Swagger UI

    http://127.0.0.1:8000/docs

### ReDoc

    http://127.0.0.1:8000/redoc

---

# ⚛️ Frontend Setup

Open a second terminal.

Navigate to the frontend directory:

    cd frontend

Install the Node.js dependencies:

    npm install

Start the development server:

    npm run dev

The frontend will normally run at:

    http://localhost:5173

Open the displayed URL in your browser.

---

# 🔌 API Endpoints

| Disease | Method | Endpoint | Features |
|---------|--------|----------|----------|
| 🩸 Diabetes | POST | `/prediction/diabetes` | 8 |
| ❤️ Heart Disease | POST | `/prediction/heart` | 13 |
| 🧠 Parkinson's Disease | POST | `/prediction/parkinsons` | 22 |

---

# 🩸 Diabetes Prediction

### Endpoint

    POST /prediction/diabetes

### Input

The API expects exactly 8 numerical features.

Example request:

    [
      6,
      148,
      72,
      35,
      0,
      33.6,
      0.627,
      50
    ]

### Example Response

    {
      "prediction": 1,
      "result": "Diabetic"
    }

---

# ❤️ Heart Disease Prediction

### Endpoint

    POST /prediction/heart

### Input

The API expects exactly 13 numerical features.

### Example Response

    {
      "prediction": 0,
      "result": "Not Heart Disease"
    }

---

# 🧠 Parkinson's Disease Prediction

### Endpoint

    POST /prediction/parkinsons

### Input

The API expects exactly 22 numerical features.

### Example Response

    {
      "prediction": 1,
      "result": "Parkinsons Disease"
    }

---

# 🤖 Machine Learning Models

The project currently uses three trained machine learning models.

    models/
    │
    ├── diabetes_model.sav
    ├── heart_disease_model.sav
    └── parkinsons_model.sav

The FastAPI backend loads these models when the application starts.

The models are used to perform predictions based on the input features provided by the frontend.

---

# 🔬 Machine Learning Workflow

    Dataset
       │
       ▼
    Data Preprocessing
       │
       ▼
    Feature Selection
       │
       ▼
    Model Training
       │
       ▼
    Model Evaluation
       │
       ▼
    Save Trained Model
       │
       ▼
    FastAPI Backend
       │
       ▼
    React Frontend
       │
       ▼
    Prediction Result

---

# 📊 Datasets

The project currently contains datasets for:

- Diabetes
- Heart Disease
- Parkinson's Disease

Datasets are located inside:

    datasets/

The original training and experimentation notebooks are located inside:

    notebook/

---

# 📓 Machine Learning Notebooks

The repository contains Jupyter notebooks used for machine learning experimentation and model development.

### Diabetes

    notebook/Multiple_disease_prediction_system_diabetes.ipynb

### Heart Disease

    notebook/Multiple_disease_prediction_system_heart.ipynb

### Parkinson's Disease

    notebook/Multiple_disease_prediction_system_Parkinsons.ipynb

These notebooks can be used to understand the data preprocessing, model training, evaluation, and prediction workflow.

---

# 🔥 My Contributions

This repository is being actively improved and extended beyond the original implementation.

### Backend Improvements

- Fixed machine learning model path handling
- Improved model loading using Python pathlib
- Added proper local development CORS configuration
- Improved API input validation
- Organized FastAPI endpoints
- Improved backend error handling

### Frontend Improvements

- Modernized the user interface
- Improved responsive design
- Improved disease selection experience
- Improved prediction result presentation
- Improved form usability

### Planned Improvements

- Authentication
- Database integration
- Prediction history
- Advanced dashboard
- Improved model evaluation
- Brain tumor detection
- CNN image classification
- Medical image upload
- AI-generated reports

> Update this section as new features are implemented.

---

# 🧠 Development Roadmap

## Phase 1 — Core System

- [x] React frontend
- [x] Vite development environment
- [x] FastAPI backend
- [x] Diabetes prediction
- [x] Heart disease prediction
- [x] Parkinson's prediction
- [x] Machine learning model integration
- [x] Pydantic validation
- [x] API documentation

---

## Phase 2 — UI/UX Improvements

- [ ] Modern healthcare dashboard
- [ ] Improved responsive design
- [ ] Better navigation
- [ ] Improved prediction forms
- [ ] Loading states
- [ ] Error states
- [ ] Better result visualization
- [ ] Accessibility improvements

---

## Phase 3 — AI Expansion

- [ ] Brain tumor detection
- [ ] CNN-based image classification
- [ ] Medical image upload
- [ ] Additional disease prediction models
- [ ] Model comparison
- [ ] Model performance dashboard

---

## Phase 4 — Full-Stack Features

- [ ] User authentication
- [ ] User profiles
- [ ] Patient profiles
- [ ] Prediction history
- [ ] Database integration
- [ ] Report generation
- [ ] Admin dashboard

---

## Phase 5 — Production

- [ ] Docker support
- [ ] Environment variables
- [ ] Secure API configuration
- [ ] HTTPS
- [ ] Rate limiting
- [ ] Logging
- [ ] Monitoring
- [ ] CI/CD
- [ ] Cloud deployment

---

# 🔮 Future Architecture

The long-term goal is to evolve the project into a modular AI healthcare platform.

                            AI Healthcare Platform
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
              ▼                   ▼                   ▼
       Disease Prediction    Image Analysis      Patient Data
              │                   │                   │
              ▼                   ▼                   ▼
       ML Classification      CNN Models        Database
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  │
                                  ▼
                           FastAPI Backend
                                  │
                                  ▼
                           React Dashboard
                                  │
                                  ▼
                          User / Patient Portal

---

# 📸 Screenshots

Screenshots of the application will be added as the interface is redesigned and new features are implemented.

Current project screenshots can be found inside:

    screenshort/

---

# 🔐 Security

This project is currently designed primarily for local development and educational purposes.

Before production deployment, additional security measures should be implemented.

Recommended improvements include:

- User authentication
- Role-based authorization
- HTTPS
- API authentication
- Rate limiting
- Input sanitization
- Secure environment variables
- Database security
- Protection of sensitive information
- Secure logging

---

# ⚠️ Medical Disclaimer

This project is intended for educational and research purposes only.

The predictions generated by the machine learning models should not be considered medical diagnoses or medical advice.

Machine learning predictions can contain errors and should not be used as a substitute for professional medical evaluation.

Always consult a qualified healthcare professional for diagnosis, treatment, or other medical decisions.

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

## 1. Fork the repository

Click the Fork button on GitHub.

## 2. Clone your fork

    git clone https://github.com/sanyamsharma062/Multi-Disease-Prediction.git

## 3. Create a feature branch

    git checkout -b feature/your-feature

## 4. Make your changes

Implement your feature or improvement.

## 5. Stage your changes

    git add .

## 6. Commit your changes

    git commit -m "Add: your feature"

## 7. Push your branch

    git push origin feature/your-feature

## 8. Open a Pull Request

Create a Pull Request on GitHub.

---

# ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

---

# 👨‍💻 Author

## Sanyam Sharma

B.Tech Computer Science & Engineering  
Specialization: Data Science

### Interests

- 🤖 Artificial Intelligence
- 🧠 Machine Learning
- 📊 Data Science
- 💻 Full-Stack Development
- 🐍 Python
- ⚡ FastAPI
- ⚛️ React
- ☁️ Cloud Technologies

---

# 📌 Project Status

    🟢 Active Development

The project is continuously being improved with new features, UI enhancements, backend improvements, and machine learning capabilities.

---

# 📄 License

This project is intended for educational and research purposes.

If this repository is based on or forked from another project, please retain the original project's license, copyright notices, and attribution requirements.

---

## 🚀 Future Goal

Build a scalable AI-powered healthcare platform that combines:

    Machine Learning
          +
    Computer Vision
          +
    FastAPI
          +
    React
          +
    Database
          +
    Cloud Deployment

    =

    🩺 AI Healthcare Platform
