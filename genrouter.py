import streamlit as st
import requests
import base64
import os

# --- App Config ---
st.set_page_config(page_title="Unified Task Router", layout="centered")

# --- (Chatbot Icon) ---
image_path = "chatbot_icon.png"  # Replace with your image path
if os.path.exists(image_path):
    with open(image_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/png;base64,{b64_image}" alt="Chatbot" width="180"/>
            <h1 style='margin-top: 10px;'>GenRouter</h1>
        </div>
    """, unsafe_allow_html=True)
else:
    st.title("🤖 GenRouter")

# --- CSS Styling ---
st.markdown("""
<style>
/* Chat container */
.chat-box {
    background-color: #f2f2f2;
    border-radius: 12px;
    padding: 15px;
    margin-top: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* User message */
.user-prompt {
    background-color: #e6f0ff;
    padding: 12px;
    border-radius: 10px;
    font-weight: 600;
    color: #0b3c5d;
    margin-bottom: 10px;
}

/* Bot message */
.bot-response {
    background-color: #e8f5e9;
    padding: 12px;
    border-radius: 10px;
    font-weight: 500;
    color: #1b5e20;
}

/* Improve textarea */
textarea {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# --- Constants ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"

# --- Prompt Router ---
def route_prompt(task_type, user_input):
    if task_type == "Q & A":
        return f"You are an expert AI. Answer the following question:\n\nQuestion: {user_input}\n\nAnswer:"
    elif task_type == "Summarization":
        return f"Summarize the following text:\n\n{user_input}\n\nSummary:"
    elif task_type == "Roleplay":
        return f"You are a compassionate doctor. Roleplay and respond to: {user_input}"
    else:
        return user_input

# --- Query Ollama ---
def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "[No response from model]")
        else:
            return f"[Error {response.status_code}] {response.text}"
    except Exception as e:
        return f"[Exception] {str(e)}"

# --- Task Selector ---
task_type = st.selectbox("Select Task Type", ["Q & A", "Summarization", "Roleplay"])

# --- Input Area ---
with st.form("user_form"):
    user_input = st.text_area("Enter your prompt", height=150)
    submitted = st.form_submit_button(label="Send")

# --- Output Area ---
if submitted and user_input:
    with st.spinner("Thinking..."):
        final_prompt = route_prompt(task_type, user_input)
        response = query_ollama(final_prompt)

    # Chat Display
    st.markdown(f"""
    <div class='chat-box'>
        <div class='user-prompt'>🧑‍💻 <strong>You:</strong><br>{user_input}</div>
        <div class='bot-response'>🤖 <strong>Bot:</strong><br>{response}</div>
    </div>
    """, unsafe_allow_html=True)
