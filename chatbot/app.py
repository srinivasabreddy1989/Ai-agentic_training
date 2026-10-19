import streamlit as st
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("HR chatbot assistant")

if "messages" not in st.session_state:
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I'm your HR chatbot assistant. How can I help you today?"})
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_input = st.text_input("Enter your message")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = openai.responses.create(
        model="gpt-4.1",
        instructions="You are a HR chatbot assistant. You are helpful and friendly. only answer questions related to HR. other questions you say i will only answer hr related questions.",
        input=user_input
    )
    st.write(response.output_text)