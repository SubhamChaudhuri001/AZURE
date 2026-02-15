import streamlit as st

st.set_page_config(page_title="HealthPredict AI",page_icon="🏩", layout="centered")

st.title("🏥 AI-Powered Multi-Disease Risk Prediction & Preventive Healthcare System")
st.caption("Machine Learning + LLM Powered Preventive Healthcare Assistant")

st.sidebar.markdown(
    """
    <div style="background-color: black; padding: 5px; border-radius: 10px;">
        <h2 style="color: white; text-align: center;">🧠<b> HealthPredict AI</b></h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("Welcome 👋")
st.write("""
This AI-powered healthcare system includes:

    ✅ Heart Disease Risk Prediction  
    ✅ Diabetes Risk Prediction  
    ✅ LLM-based Personalized Health Advice  
    ✅ Downloadable AI-Generated PDF Reports  
    ✅ Interactive Healthcare Chatbot  

    ⚠️ This system is for educational purposes only.
    It does not replace professional medical consultation.
    """)