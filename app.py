import streamlit as st
from google_sheet import get_sheet_data
import google.generativeai as genai

st.set_page_config(page_title="AI Agent", page_icon="🤖", layout="wide")
st.title("AI Agent 🤖")
st.write("Ask me anything. Built By Manzar🤖.")

API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

if "chat" not in st.session_state:
    st.session_state.chat = []

prompt = st.chat_input("👋 Hi, I'm Manzar!")
if prompt:
    st.session_state.chat.append({"role": "user", "content": prompt})
    sheet_data = get_sheet_data()
    context = f"Knowledge base:\n{sheet_data}\n\nUser asked: {prompt}"
    response = model.generate_content(context)
    st.session_state.chat.append({"role": "agent", "content": response.text})

for msg in st.session_state.chat:
    st.chat_message(msg["role"]).markdown(msg["content"])
