import streamlit as st
import requests
import base64
import os

# --- App Config ---
st.set_page_config(page_title="🤖 GenRouter - Virtual Assistant", layout="centered")

# --- Chatbot Icon & Title ---
image_path = "chatbot_icon.png"
if os.path.exists(image_path):
    with open(image_path, "rb") as img_file:
        b64_image = base64.b64encode(img_file.read()).decode()
    st.markdown(f"""
        <div style='text-align: center;'>
            <img src="data:image/png;base64,{b64_image}" alt="Chatbot" width="180"/>
        </div>
    """, unsafe_allow_html=True)

# Centered Title
st.markdown("<h1 style='text-align: center; margin-bottom: 0;'>🤖 GenRouter</h1>", unsafe_allow_html=True)

# --- CSS Styling ---
st.markdown("""
<style>
.chat-box {
    background-color: #f2f2f2;
    border-radius: 12px;
    padding: 15px;
    margin-top: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.user-prompt {
    background-color: #e6f0ff;
    padding: 12px;
    border-radius: 10px;
    font-weight: 600;
    color: #0b3c5d;
    margin-bottom: 10px;
}
.bot-response {
    background-color: #e8f5e9;
    padding: 12px;
    border-radius: 10px;
    font-weight: 500;
    color: #1b5e20;
}
textarea {
    font-size: 16px !important;
}
</style>
""", unsafe_allow_html=True)

# --- Constants ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"

# --- Prompt Router ---
def route_prompt(task_type, user_input, role_type=None):
    if task_type == "Q & A":
        return f"You are an expert AI. Answer the following question:\n\nQuestion: {user_input}\n\nAnswer:"
    elif task_type == "Summarization":
        return f"Summarize the following text:\n\n{user_input}\n\nSummary:"
    elif task_type == "Roleplay":
        if role_type == "Doctor":
            return f"You are a compassionate doctor. Respond to the following:\n{user_input}"
        elif role_type == "Lawyer":
            return f"You are a professional lawyer. Respond to the following legal scenario:\n{user_input}"
        elif role_type == "Customer Support Agent":
            return f"You are a polite customer support agent. Help with the following issue:\n{user_input}"
        else:
            return f"Respond to this as a fictional roleplay character:\n{user_input}"
    elif task_type == "Translation":
        return f"Translate the following text into fluent English:\n\n{user_input}"
    elif task_type == "JSON Mode and Structured Output Generator":
        return f"Convert the following into a structured JSON format, maintaining all important information:\n\n{user_input}"
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

# --- Task Selection ---
task_type = st.selectbox("Select Task Type", [
    "Q & A",
    "Summarization",
    "Roleplay",
    "Translation",
    "JSON Mode and Structured Output Generator"
])

# --- Roleplay Character Selection ---
role_type = None
if task_type == "Roleplay":
    role_type = st.radio("Choose Roleplay Character", ["Doctor", "Lawyer", "Customer Support Agent"], horizontal=True)

# --- Input Form ---
with st.form("user_form"):
    user_input = st.text_area("Enter your prompt", height=150)
    submitted = st.form_submit_button(label="Send")

# --- Output ---
if submitted and user_input:
    with st.spinner("Thinking..."):
        final_prompt = route_prompt(task_type, user_input, role_type)
        response = query_ollama(final_prompt)

    # Chat Display
    st.markdown(f"""
    <div class='chat-box'>
        <div class='user-prompt'>🧑‍💻 <strong>You:</strong><br>{user_input}</div>
        <div class='bot-response'>🤖 <strong>GenRouter:</strong><br>{response}</div>
    </div>
    """, unsafe_allow_html=True)