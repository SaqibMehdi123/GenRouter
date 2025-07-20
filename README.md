# 🤖 GenRouter - Virtual Assistant

GenRouter is a customizable, lightweight Streamlit-based virtual assistant designed to handle multiple types of tasks — including Q&A, summarization, translation, roleplay simulation, and JSON generation — powered by the locally hosted **Gemma 3:4b** LLM using **Ollama**.

---

## 🧠 Features

- 🔍 **Q&A** – Ask any question, get expert-level answers.
- ✂️ **Summarization** – Summarize long texts into concise insights.
- 🗣️ **Roleplay** – Simulate conversations with a Doctor, Lawyer, or Support Agent.
- 🌐 **Translation** – Translate text into fluent English.
- 📊 **JSON Formatter** – Convert input into structured JSON output.

---

## 📦 Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io)
- [Ollama](https://ollama.com) installed and running locally
- `gemma3:4b` model pulled using Ollama

---

## 🚀 Installation & Running

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/genrouter-assistant.git
cd genrouter-assistant
```

### 2. Create & Activate a Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
If requirements.txt doesn’t exist, install manually:
```bash
pip install streamlit requests
```

### 4. Pull the Gemma 3:4b Model via Ollama
Make sure you have Ollama installed, then run:
```bash
ollama pull gemma:4b
```

### 5. Run the App
```bash
streamlit run app.py
```
Replace app.py with your filename if different.

---

## 🖼️ UI Layout
- Centered Title & Logo
- Selectbox for Task Type
- Dynamic Role Selector for Roleplay
- Text Area Input
- Stylized Chat Box with Bot and User Messages

---

## ⚙️ Code Structure
- route_prompt() handles prompt formatting based on task type.
- query_ollama() sends the prompt to the local LLM via REST API.
- HTML & CSS embedded in Streamlit for clean UI styling.
- Chat interaction is shown in a neatly styled box.

---

## 🧑‍💻 Author
Made by [Saqib Mehdi](https://github.com/SaqibMehdi123)

---

## 📜 License
MIT License — feel free to use and modify!

