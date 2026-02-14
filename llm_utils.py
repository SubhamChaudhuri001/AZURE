from huggingface_hub import InferenceClient
import streamlit as st

# Get token safely
HF_TOKEN = st.secrets["HF_API_TOKEN"]

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=HF_TOKEN
)

def generate_health_advice(prompt, max_tokens=500):

    messages = [
        {"role": "system", "content": "You are a professional medical AI assistant. Provide short, practical lifestyle advice."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat_completion(
        messages=messages,
        max_tokens=max_tokens,
        temperature=0.6
    )

    return response.choices[0].message["content"]
