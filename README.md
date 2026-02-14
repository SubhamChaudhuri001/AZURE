
# 🏥 HealthPredict AI — AI-Powered Multi-Disease Risk Prediction & Preventive Healthcare System

HealthPredict AI is a full-stack AI-powered healthcare web application that predicts the risk of Heart Disease and Diabetes using Machine Learning models and provides intelligent health guidance using Generative AI.

This system combines:

- Predictive Machine Learning
- Generative AI (LLM-based health assistant)
- Interactive Web UI
- Automated PDF health reporting

Built for real-world preventive healthcare assistance and academic demonstration.

## 🚀 Key Features

- ❤️ Heart Disease Risk Prediction (ML-based)
- 🩸 Diabetes Risk Prediction (ML-based)
- 📊 Probability-based risk scoring
- 🤖 AI-powered personalized health advice (LLM)
- 💬 Interactive healthcare chatbot
- 📄 Downloadable PDF health report
- 🔐 Secure API key handling using Streamlit Secrets
- 🖥 Multi-page professional Streamlit interface

## 📊 Machine Learning

- Algorithm: Logistic Regression
- Feature Scaling using StandardScaler
- Cleaned and preprocessed healthcare datasets
- Probability-based output for risk interpretation
- Model trained separately and deployed using .pkl files

## 🧠 Technologies Used

 Category         | Tools                                 
 ---------------- | ------------------------------------- 
 Language         | Python  
 Frontend         | Streamlit                             
 Machine Learning | Scikit-learn                          
 Generative AI    | HuggingFace Inference API (Llama 3.1) 
 Data Handling    | Pandas, NumPy                         
 PDF Generation   | ReportLab               
 Model Storage    | Pickle
 Deployment       | Streamlit Cloud / HuggingFace Spaces  



## 📁 Project Structure

HealthPredictAI/
│
├── Main_APP.py
├── pages/
│   ├── 1_Heart_Disease.py
│   ├── 2_Diabetes.py
│   └── 3_Chatbot.py
│
├── models/
│   ├── train_heart_model.py
│   ├── train_diabetes_model.py
│   ├── heart_model.pkl
│   └── diabetes_model.pkl
│
├── data/
│   ├── heart.csv
│   └── diabetes_risk_dataset.csv
│
├── assets/
│   └── healthpredict_logo.png
│
├── llm_utils.py
├── requirements.txt
└── .streamlit/
    └── secrets.toml

## ▶️ How to Run the Project

1️⃣ Clone the Repository

git clone <your-repo-link>
cd HealthPredictAI

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Add API Key

Create a file:

.streamlit/secrets.toml

Add:
HUGGINGFACE_API_KEY = "your_api_key_here"

4️⃣ Run the App

streamlit run Main_APP.py

## 📊 Future Enhancements

- 🌍 Multilingual Support
- 🎤 Voice-Based Interaction
- 📱 Cross-platform Mobile App (Flutter / React Native)
- ☁ Cloud Database Integration
- 📈 Model Performance Dashboard
- 🔬 Additional Disease Prediction Modules

## ⚠ Disclaimer

This application is developed for educational and preventive healthcare purposes only.
It does not replace professional medical advice, diagnosis, or treatment.


