# 🧠 Multi-Disease Prediction System

> **AI/ML-powered Full-Stack Healthcare Prediction Platform**

A full-stack **Multi-Disease Prediction System** that uses Machine Learning models to predict the likelihood of multiple diseases through a web-based interface.

The current system supports:

- 🩸 Diabetes Prediction
- ❤️ Heart Disease Prediction
- 🧠 Parkinson's Disease Prediction

The project combines **Machine Learning, Python, FastAPI, React, Vite, and REST APIs** into a unified healthcare-oriented application.

> **Project Status:** 🚧 Active Development  
> **Project Type:** Final Year BTech Project  
> **Domain:** Artificial Intelligence / Machine Learning / Healthcare  
> **Frontend:** React + Vite  
> **Backend:** FastAPI  
> **ML:** Scikit-learn

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Motivation](#motivation)
- [Project Objectives](#project-objectives)
- [Proposed Solution](#proposed-solution)
- [How the System Works](#how-the-system-works)
- [Supported Diseases](#supported-diseases)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Machine Learning Workflow](#machine-learning-workflow)
- [Datasets](#datasets)
- [Machine Learning Notebooks](#machine-learning-notebooks)
- [Feature Requirements](#feature-requirements)
- [Machine Learning Models](#machine-learning-models)
- [Backend Architecture](#backend-architecture)
- [Frontend Architecture](#frontend-architecture)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Input Validation](#input-validation)
- [CORS Configuration](#cors-configuration)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [Testing the API](#testing-the-api)
- [Prediction Flow](#prediction-flow)
- [Error Handling](#error-handling)
- [Advantages](#advantages)
- [Current Limitations](#current-limitations)
- [My Contributions](#my-contributions)
- [Development Roadmap](#development-roadmap)
- [Future Scope](#future-scope)
- [Security Considerations](#security-considerations)
- [Screenshots](#screenshots)
- [Academic Relevance](#academic-relevance)
- [Learning Outcomes](#learning-outcomes)
- [Medical Disclaimer](#medical-disclaimer)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)
- [Project Vision](#project-vision)
- [Project Status](#project-status)

---

## 📌 Project Overview

The **Multi-Disease Prediction System** is designed to demonstrate how Machine Learning can be integrated into a practical healthcare application.

Instead of developing separate applications for every disease, the project provides a unified platform where users can select a disease and enter the required medical parameters.

The backend processes the input using a trained Machine Learning model and returns the prediction through a REST API.

### Current Prediction Modules

| Disease | Required Features | Model | Status |
|---|---:|---|---|
| Diabetes | 8 numerical features | Scikit-learn | ✅ Available |
| Heart Disease | 13 numerical features | Scikit-learn | ✅ Available |
| Parkinson's Disease | 22 numerical features | Scikit-learn | ✅ Available |
| Brain Tumor | Medical image | CNN / Deep Learning | 🔜 Planned |

---

## ❗ Problem Statement

Many healthcare prediction systems are developed as isolated Machine Learning experiments.

Common challenges include:

- Machine Learning models are not integrated into usable applications.
- Different disease prediction models often require separate interfaces.
- Raw ML notebooks are difficult for non-technical users to interact with.
- ML models need a proper API layer before they can be integrated into applications.
- Healthcare-oriented ML projects require clear input validation and error handling.
- A scalable architecture is needed to add additional disease prediction modules.

This project addresses these challenges by combining multiple disease prediction models into a single full-stack application.

---

## 💡 Motivation

The motivation behind this project is to understand how Machine Learning can move from a notebook-based experiment to a practical software application.

The project provides practical experience in:

- Machine Learning
- Data preprocessing
- Model training
- Model serialization
- REST API development
- Backend development
- Frontend development
- API integration
- Input validation
- Full-stack application architecture

---

## 🎯 Project Objectives

The major objectives of this project are:

1. Develop Machine Learning models for multiple diseases.
2. Process healthcare datasets for model training.
3. Serialize trained models for application use.
4. Develop a FastAPI backend.
5. Create REST API endpoints for predictions.
6. Validate user input before prediction.
7. Develop a React-based frontend.
8. Connect the frontend with the FastAPI backend.
9. Provide a unified interface for multiple diseases.
10. Create a scalable architecture for future disease models.
11. Improve the application UI/UX.
12. Evaluate and improve Machine Learning models.
13. Explore future integration of advanced AI models such as CNNs.

---

## 🧩 Proposed Solution

The system consists of four major layers:

```text
┌─────────────────────────────────────┐
│           User Interface            │
│         React + Vite Frontend       │
└──────────────────┬──────────────────┘
                   │
                   │ HTTP / REST API
                   ▼
┌─────────────────────────────────────┐
│           FastAPI Backend           │
│      Validation + Prediction API    │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          Serialized ML Models       │
│          Scikit-learn / Pickle      │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│             Datasets                │
│ Diabetes / Heart / Parkinson's      │
└─────────────────────────────────────┘
```

---

## ⚙️ How the System Works

The application follows this general process:

```text
User
  │
  ▼
Select Disease
  │
  ▼
Enter Required Medical Parameters
  │
  ▼
Frontend Validation
  │
  ▼
Send JSON Request
  │
  ▼
FastAPI Backend
  │
  ▼
Pydantic Input Validation
  │
  ▼
Load Appropriate ML Model
  │
  ▼
Generate Prediction
  │
  ▼
Return JSON Response
  │
  ▼
React Frontend
  │
  ▼
Display Prediction Result
```

---

## 🩺 Supported Diseases

### 1. Diabetes

The Diabetes prediction model currently expects **8 numerical input features**.

Endpoint:

```text
POST /prediction/diabetes
```

Possible results:

```text
Diabetic
Not Diabetic
```

### 2. Heart Disease

The Heart Disease prediction model currently expects **13 numerical input features**.

Endpoint:

```text
POST /prediction/heart
```

Possible results:

```text
Heart Disease
Not Heart Disease
```

### 3. Parkinson's Disease

The Parkinson's Disease model currently expects **22 numerical input features**.

Endpoint:

```text
POST /prediction/parkinsons
```

Possible results:

```text
Parkinsons Disease
Not Parkinsons Disease
```

### 4. Brain Tumor Detection

Brain Tumor Detection is planned as a future extension.

The planned implementation may include:

- Medical image upload
- Image preprocessing
- Convolutional Neural Network
- Deep Learning classification
- Prediction confidence
- Image-based results

This feature is **not currently implemented**.

---

## 🏗️ System Architecture

The current architecture is:

```text
                         ┌─────────────────┐
                         │      User       │
                         └────────┬────────┘
                                  │
                                  ▼
                     ┌────────────────────────┐
                     │   React + Vite UI      │
                     │       Frontend         │
                     └───────────┬────────────┘
                                 │
                                 │ HTTP / JSON
                                 ▼
                     ┌────────────────────────┐
                     │       FastAPI          │
                     │       Backend          │
                     └───────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
       ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
       │  Diabetes   │    │    Heart    │    │ Parkinson's │
       │    Model    │    │    Model    │    │    Model    │
       └─────────────┘    └─────────────┘    └─────────────┘
```

---

## 🛠️ Technology Stack

### Frontend

| Technology | Purpose |
|---|---|
| React | User Interface |
| Vite | Frontend Development Tool |
| JavaScript | Application Logic |
| CSS | Styling |
| Fetch API | Backend Communication |

### Backend

| Technology | Purpose |
|---|---|
| Python | Backend and ML |
| FastAPI | REST API |
| Pydantic | Input Validation |
| Uvicorn | ASGI Server |
| NumPy | Numerical Processing |

### Machine Learning

| Technology | Purpose |
|---|---|
| Scikit-learn | Machine Learning |
| Pandas | Dataset Processing |
| NumPy | Numerical Computation |
| Pickle | Model Serialization |
| Jupyter Notebook | ML Development |

### Development Tools

- Git
- GitHub
- VS Code / Cursor
- Terminal
- Python Virtual Environment
- npm

---

## 📂 Project Structure

The current project structure is:

```text
Multi-Disease-Prediction-main/
│
├── README.md
├── package-lock.json
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
├── notebook/
│   ├── Multiple_disease_prediction_system_Parkinsons.ipynb
│   ├── Multiple_disease_prediction_system_diabetes.ipynb
│   └── Multiple_disease_prediction_system_heart.ipynb
│
├── frontend/
│   ├── README.md
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   │
│   └── src/
│       ├── App.jsx
│       ├── main.jsx
│       ├── diseaseData.js
│       ├── styles.css
│       └── assets/
│
├── screenshort/
│   ├── dashboard.jpg.jpeg
│   ├── home.jpg.jpeg
│   ├── location.jpg.jpeg
│   └── login.jpg.jpeg
│
└── path/
    └── to/
        └── venv/
```

### GitHub Repository Hygiene

The following are normally local/generated development artifacts and should not be committed:

```text
.venv/
__pycache__/
node_modules/
*.pyc
.env
```

A `.gitignore` file should be used to exclude them.

---

## 🤖 Machine Learning Workflow

The Machine Learning workflow follows:

```text
Dataset
   │
   ▼
Data Exploration
   │
   ▼
Data Cleaning
   │
   ▼
Preprocessing
   │
   ▼
Feature Selection
   │
   ▼
Train / Test Split
   │
   ▼
Model Training
   │
   ▼
Model Evaluation
   │
   ▼
Model Serialization
   │
   ▼
FastAPI Integration
   │
   ▼
Prediction
```

---

## 📊 Datasets

The project currently contains three datasets:

```text
datasets/
├── diabetes.csv
├── heart.csv
└── parkinsons.csv
```

These datasets are used for developing the corresponding prediction models.

For an academic or production release, dataset sources, licenses, feature definitions, preprocessing decisions, and data limitations should be documented clearly.

---

## 📓 Machine Learning Notebooks

The Machine Learning development notebooks are stored in:

```text
notebook/
```

Current notebooks:

```text
Multiple_disease_prediction_system_diabetes.ipynb
Multiple_disease_prediction_system_heart.ipynb
Multiple_disease_prediction_system_Parkinsons.ipynb
```

The notebooks contain the experimental Machine Learning workflow used to develop the prediction models.

---

## 🔢 Feature Requirements

The FastAPI backend validates the number of features submitted to each prediction endpoint.

| Prediction Module | Required Features |
|---|---:|
| Diabetes | 8 |
| Heart Disease | 13 |
| Parkinson's Disease | 22 |

The backend rejects requests containing an incorrect number of features.

> **Important:** The exact feature order must match the order used when the corresponding model was trained.

---

## 🧠 Machine Learning Models

Serialized models are stored in:

```text
models/
```

Current models:

```text
diabetes_model.sav
heart_disease_model.sav
parkinsons_model.sav
```

The FastAPI backend loads these models when the application starts.

Model files can be sensitive to the Python and scikit-learn versions used during training. The project should therefore preserve compatible dependency versions when models are serialized with pickle.

---

## 🔙 Backend Architecture

The backend is implemented using FastAPI.

Main backend file:

```text
backend/main.py
```

The backend provides:

- REST API endpoints
- Request validation
- Model loading
- Prediction processing
- Error handling
- CORS configuration

### Model Directory

The project stores models at the project root:

```text
Multi-Disease-Prediction-main/
├── backend/
│   └── main.py
│
└── models/
    ├── diabetes_model.sav
    ├── heart_disease_model.sav
    └── parkinsons_model.sav
```

The backend uses a project-root-relative path for loading these files. This prevents errors caused by starting the server from a different working directory.

---

## 🎨 Frontend Architecture

The frontend is located inside:

```text
frontend/
```

Main files:

```text
frontend/
├── index.html
├── package.json
├── vite.config.js
└── src/
    ├── App.jsx
    ├── main.jsx
    ├── diseaseData.js
    └── styles.css
```

### Frontend Responsibilities

The React frontend handles:

- User interface
- Disease selection
- Input forms
- API requests
- Prediction results
- User interaction
- Styling
- Frontend-side validation

---

## 🔌 API Documentation

FastAPI automatically provides interactive API documentation.

After starting the backend, open:

```text
http://127.0.0.1:8000/docs
```

Alternative documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## 🌐 API Endpoints

### Health Check

```text
GET /
```

Example response:

```json
{
  "message": "Multi Disease Prediction API is running"
}
```

### Diabetes Prediction

```text
POST /prediction/diabetes
```

Request body format:

```json
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
```

Example response:

```json
{
  "prediction": 1,
  "result": "Diabetic"
}
```

### Heart Disease Prediction

```text
POST /prediction/heart
```

Request body format:

```json
[
  63,
  1,
  3,
  145,
  233,
  1,
  0,
  150,
  0,
  2.3,
  0,
  0,
  1
]
```

Example response:

```json
{
  "prediction": 1,
  "result": "Heart Disease"
}
```

### Parkinson's Prediction

```text
POST /prediction/parkinsons
```

Request body format:

```json
[
  119.992,
  157.302,
  74.997,
  0.00784,
  0.00007,
  0.00370,
  0.00554,
  0.01109,
  0.04374,
  0.426,
  0.02182,
  0.03130,
  0.02971,
  0.06545,
  0.02211,
  21.033,
  0.414783,
  0.815285,
  -4.813031,
  -4.075192,
  2.286502,
  0.665415
]
```

Example response:

```json
{
  "prediction": 1,
  "result": "Parkinsons Disease"
}
```

> **Important:** The sample payloads illustrate the API format. The exact feature names, meaning, scale, and ordering must match the corresponding training dataset/model.

---

## ✅ Input Validation

The backend uses Pydantic validation classes to verify the number of input features.

Current requirements:

```text
Diabetes      → 8 features
Heart Disease → 13 features
Parkinson's   → 22 features
```

Invalid feature counts are rejected before the model prediction is executed.

This reduces errors caused by incomplete or incorrectly structured API requests.

---

## 🔐 CORS Configuration

The backend is configured for the local React development server.

Allowed development origins include:

```text
http://localhost:5173
http://127.0.0.1:5173
```

The local frontend should not be configured as HTTPS unless an HTTPS development server has actually been set up.

For production deployment, CORS should be restricted to the actual frontend domain rather than allowing arbitrary origins.

---

## 📥 Installation

### Prerequisites

Install:

- Python 3.13 or another compatible Python version
- Node.js
- npm
- Git

Verify the installations:

```bash
python3 --version
node --version
npm --version
git --version
```

---

## 🐍 Backend Setup

From the project root:

```bash
cd Multi-Disease-Prediction-main
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install Python dependencies:

```bash
python3 -m pip install -r requirements.txt
```

If the repository does not yet contain `requirements.txt`, create it using the dependency versions maintained by the project.

Example:

```text
fastapi==0.141.1
uvicorn[standard]==0.53.0
pydantic==2.13.5
numpy==2.5.3
pandas
scikit-learn==1.9.1
scipy==1.18.1
joblib==1.6.0
cloudpickle==3.1.2
```

> Keep the scikit-learn and related versions compatible with the serialized `.sav` models.

---

## ⚛️ Frontend Setup

Open a second terminal.

Navigate to the frontend:

```bash
cd Multi-Disease-Prediction-main/frontend
```

Install dependencies:

```bash
npm install
```

---

## ▶️ Running the Application

### Terminal 1 — Start Backend

From the project root:

```bash
cd Multi-Disease-Prediction-main
source .venv/bin/activate
uvicorn backend.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Terminal 2 — Start Frontend

```bash
cd Multi-Disease-Prediction-main/frontend
npm run dev
```

Frontend:

```text
http://localhost:5173
```

Open the frontend in your browser:

```text
http://localhost:5173
```

---

## 🧪 Testing the API

The API can be tested using:

- FastAPI Swagger UI
- cURL
- Postman
- Frontend application

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### cURL Example

Example Diabetes request:

```bash
curl -X POST "http://127.0.0.1:8000/prediction/diabetes" \
-H "Content-Type: application/json" \
-d '[6,148,72,35,0,33.6,0.627,50]'
```

---

## 🔄 Prediction Flow

The complete prediction flow is:

```text
React Form
     │
     ▼
User Input
     │
     ▼
Frontend Validation
     │
     ▼
POST /prediction/<disease>
     │
     ▼
FastAPI
     │
     ▼
Pydantic Validation
     │
     ▼
NumPy Array
     │
     ▼
Selected ML Model
     │
     ▼
Prediction
     │
     ▼
JSON Response
     │
     ▼
React Frontend
     │
     ▼
Prediction Result
```

---

## ⚠️ Error Handling

The backend handles prediction errors using FastAPI's `HTTPException`.

For example:

```json
{
  "detail": "Diabetes prediction failed. Please try again."
}
```

Similar error handling is implemented for:

- Diabetes
- Heart Disease
- Parkinson's Disease

The system also validates the expected number of input features before attempting prediction.

---

## ⭐ Advantages

The current system provides:

- Multiple disease predictions in one application
- Machine Learning integration
- REST API architecture
- React frontend
- FastAPI backend
- Pydantic validation
- Modular disease endpoints
- Serialized ML models
- Interactive API documentation
- Expandable architecture
- Suitable foundation for a final-year academic project

---

## ⚠️ Current Limitations

The current version has several limitations:

- Predictions depend on the quality of the trained models and datasets.
- No user authentication is currently implemented.
- No database-backed prediction history is currently implemented.
- No doctor/admin dashboard is currently implemented.
- Brain Tumor CNN detection is not yet implemented.
- Production deployment configuration is not yet finalized.
- Clinical validation has not been performed.
- The current models should not be treated as clinically validated diagnostic systems.
- Prediction outputs do not replace professional medical evaluation.

---

## 👨‍💻 My Contributions

This repository is based on an existing Multi-Disease Prediction project that has been forked and extended for academic development.

My work focuses on improving the existing implementation and developing it into a more structured full-stack final-year project.

### Current Contributions

#### Backend Improvements

- Fixed model path handling.
- Added project-root-relative model paths using `pathlib`.
- Improved CORS configuration for local React development.
- Added input-length validation.
- Structured disease prediction endpoints.
- Added FastAPI error handling.
- Integrated serialized ML models with the API.

#### Full-Stack Development

- Integrated React + Vite frontend.
- Connected frontend forms with FastAPI prediction endpoints.
- Organized frontend disease configuration/data.
- Developed a unified disease prediction interface.

#### Project Documentation

- Restructured project documentation.
- Added system architecture documentation.
- Documented API endpoints.
- Documented installation and execution steps.
- Added limitations and future scope.
- Added a phased development roadmap.

### Planned Contributions

The following are part of ongoing development and are not claimed as completed:

- Improved UI/UX
- Better prediction result presentation
- ML model evaluation
- Model performance comparison
- Prediction history
- User authentication
- Database integration
- PDF reports
- Brain Tumor CNN module
- Production deployment

---

## 🗺️ Development Roadmap

### Phase 1 — Core System

- [x] Diabetes prediction
- [x] Heart disease prediction
- [x] Parkinson's prediction
- [x] FastAPI backend
- [x] REST API endpoints
- [x] Input validation
- [x] React + Vite frontend
- [x] Frontend-backend integration

### Phase 2 — UI/UX Improvements

- [ ] Modern dashboard
- [ ] Responsive design
- [ ] Improved prediction cards
- [ ] Form validation messages
- [ ] Loading indicators
- [ ] Error-state UI
- [ ] Accessibility improvements
- [ ] Better mobile experience

### Phase 3 — Machine Learning Improvements

- [ ] Model performance comparison
- [ ] Accuracy analysis
- [ ] Precision / Recall / F1-score
- [ ] Confusion matrices
- [ ] ROC-AUC analysis
- [ ] Cross-validation
- [ ] Feature importance
- [ ] Hyperparameter tuning
- [ ] Model version tracking

### Phase 4 — AI Expansion

- [ ] Brain Tumor Detection
- [ ] CNN-based image classification
- [ ] Medical image preprocessing
- [ ] Image upload interface
- [ ] Prediction confidence visualization

### Phase 5 — Full-Stack Features

- [ ] User authentication
- [ ] User profiles
- [ ] Database integration
- [ ] Prediction history
- [ ] Saved reports
- [ ] PDF report generation
- [ ] Admin dashboard

### Phase 6 — Production

- [ ] Docker
- [ ] Environment variables
- [ ] HTTPS
- [ ] API rate limiting
- [ ] Logging
- [ ] Monitoring
- [ ] CI/CD
- [ ] Cloud deployment
- [ ] Production security

---

## 🔮 Future Scope

The system can be expanded into a broader AI-assisted healthcare platform.

### Additional Disease Prediction

Potential future modules include:

- Liver Disease
- Kidney Disease
- Breast Cancer
- Thyroid Disease
- Anemia
- Stroke Risk
- Lung Disease

### Advanced AI

Future research directions include:

- Deep Learning
- CNN
- Explainable AI
- Model interpretability
- Ensemble models
- Confidence estimation

### Application Features

Future application features may include:

- User accounts
- Medical history
- Prediction history
- PDF reports
- Doctor dashboard
- Admin dashboard
- Notifications
- Health analytics

---

## 🔒 Security Considerations

Before production deployment, the following should be implemented:

- HTTPS
- Secure authentication
- Password hashing
- JWT or secure session management
- Environment variables for secrets
- Input sanitization
- API rate limiting
- Restricted CORS
- Request logging
- Error monitoring
- Database security
- Role-based access control
- Protection of sensitive health information

No passwords, API keys, tokens, or other secrets should be committed to the repository.

---

## 🖼️ Screenshots

Screenshots are currently stored inside:

```text
screenshort/
```

Current screenshot files:

```text
dashboard.jpg.jpeg
home.jpg.jpeg
location.jpg.jpeg
login.jpg.jpeg
```

Example GitHub Markdown:

```markdown
![Home](screenshort/home.jpg.jpeg)
```

```markdown
![Dashboard](screenshort/dashboard.jpg.jpeg)
```

```markdown
![Login](screenshort/login.jpg.jpeg)
```

```markdown
![Location](screenshort/location.jpg.jpeg)
```

---

## 🎓 Academic Relevance

This project demonstrates the practical application of multiple Computer Science concepts.

### Machine Learning

- Supervised Learning
- Classification
- Dataset preprocessing
- Feature selection
- Model evaluation
- Model serialization

### Software Engineering

- Modular architecture
- REST APIs
- Frontend-backend separation
- Error handling
- Input validation
- Version control

### Web Development

- React
- Vite
- FastAPI
- HTTP
- JSON
- REST API integration

### Data Science

- Dataset analysis
- Numerical processing
- Feature engineering
- Model evaluation
- Prediction

---

## 📚 Learning Outcomes

Through this project, the following skills are developed:

- Python programming
- Machine Learning
- Data preprocessing
- Scikit-learn
- FastAPI
- REST API development
- React development
- JavaScript
- API integration
- Git and GitHub
- Full-stack architecture
- Software debugging
- Project documentation

---

## 🩺 Medical Disclaimer

This application is developed for **educational and research purposes only**.

The predictions generated by this system are based on Machine Learning models and the datasets used to train them.

They should **not** be considered a medical diagnosis, medical advice, or a replacement for a qualified healthcare professional.

Users should consult a qualified medical professional for actual medical evaluation and treatment decisions.

---

## 🤝 Contributing

Contributions and suggestions are welcome.

### Clone the Repository

```bash
git clone <repository-url>
cd Multi-Disease-Prediction-main
```

### Create a Feature Branch

```bash
git checkout -b feature/new-feature
```

### Make Changes

```bash
git add .
git commit -m "Add new feature"
```

### Push the Branch

```bash
git push origin feature/new-feature
```

Then create a Pull Request on GitHub.

---

## 👨‍🎓 Author

### Sanyam Sharma

**BTech — Computer Science & Engineering**  
**Specialization — Data Science**

Areas of interest:

- Data Science
- Artificial Intelligence
- Machine Learning
- Full-Stack Development
- Software Engineering

---

## 📄 License

This project is based on an existing/forked project.

Before publishing a final license for the complete repository, verify:

1. The original repository's license.
2. The licenses of all datasets.
3. The licenses of any third-party libraries/assets.
4. Any restrictions associated with the serialized models.

The original project's licensing terms should be respected for the portions derived from the upstream repository.

---

## 🚀 Project Vision

The long-term vision is to transform the current multi-disease prediction application into a more complete **AI-assisted healthcare platform**.

The planned architecture is:

```text
                    AI Healthcare Platform
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
   Disease ML          Medical Images       Analytics
   Prediction             / CNN              Dashboard
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
                    FastAPI Backend
                            │
                            ▼
                    Database / Users
                            │
                            ▼
                     React Frontend
```

The goal is to progressively improve the system from a basic Machine Learning demonstration into a structured full-stack academic project with:

- Stronger ML evaluation
- Better user experience
- Additional AI capabilities
- Secure application architecture
- Database-backed features
- Production-oriented engineering
- Scalable disease modules

---

## 📌 Project Status

```text
Project Type          : Final Year BTech Project
Development Status    : Active Development
Frontend              : React + Vite
Backend               : FastAPI
Machine Learning      : Scikit-learn
Prediction Modules    : 3
Prediction APIs       : 3
Brain Tumor CNN       : Planned
Authentication        : Planned
Database              : Planned
Prediction History    : Planned
PDF Reports           : Planned
Production Deployment : Planned
```

---

## ⭐ Final Note

This project brings together:

**Data Science + Machine Learning + Backend Development + Frontend Development + REST APIs + Software Engineering**

The architecture is designed so that additional disease prediction models and application features can be added without rebuilding the entire system.

**Built as an academic project with a focus on practical AI/ML and full-stack development.**
