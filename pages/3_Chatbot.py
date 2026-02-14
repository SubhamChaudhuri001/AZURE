import streamlit as st
import time
from llm_utils import generate_health_advice

st.set_page_config(page_title="HealthPredict AI (AI Healthcare Chatbot)",page_icon="🏩", layout="centered")

st.sidebar.markdown(
    """
    <div style="background-color: black; padding: 5px; border-radius: 10px;">
        <h2 style="color: white; text-align: center;">🧠<b> HealthPredict AI</b></h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.header("👨‍⚕️ AI Healthcare Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("♻️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your health question..."):

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # SHOW USER MESSAGE IMMEDIATELY
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        with st.spinner("👽 AI is thinking... 📑"):

            conversation = ""
            for msg in st.session_state.messages:
                conversation += f"{msg['role']}: {msg['content']}\n"

            response = generate_health_advice(conversation)

        # Typing effect
        for chunk in response.split():
            full_response += chunk + " "
            message_placeholder.markdown(full_response + "▌")
            time.sleep(0.03)

        message_placeholder.markdown(full_response)

    # Save assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
