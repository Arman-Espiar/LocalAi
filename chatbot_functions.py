"""
Chatbot Functions
"""

import streamlit as st
import chatbot_constants as constants
import time
from groq import Groq
from dotenv import load_dotenv
from ollama import Client

def set_page_config() -> None:
    st.set_page_config(page_title=constants.PAGE_TITLE, page_icon="👋", layout="wide")
    st.markdown(body=constants.STREAMLIT_STYLE, unsafe_allow_html=True)


def initial_session_state() -> None:
    if "model_name" not in st.session_state:
        st.session_state.model_name = constants.GROQ_MODELS[0]

    if "messages" not in st.session_state:
        st.session_state.messages = [constants.SYSTEM_MESSAGE]

    if "type_of_model" not in st.session_state:
        st.session_state.type_of_model = constants.TYPE_OF_MODEL[0]
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.8

def add_online_groq_models() -> None:
    """
    Add Online Groq Models
    """
    load_dotenv()
    client = Groq()

    models = client.models.list()
    data = models.data

    new_data = [model.id for model in data]
    new_data.sort()

    for model in new_data:
        if model not in constants.GROQ_MODELS:
         constants.GROQ_MODELS.append(model)

def chat_completion_groq(
    messages: list, model_name: str = constants.LOCAL_MODELS[0], temperature: float = 0.8
) -> str:
    """
    Groq Chat Completion Function
    """

    load_dotenv()
    client = Groq()

    chat_completion = client.chat.completions.create(
        model=model_name, messages=messages, temperature=temperature
    )

    assistant_answer: str | None = chat_completion.choices[0].message.content

    if not assistant_answer:
        assistant_answer = constants.NOT_FOUND

    return assistant_answer

def chat_completion_local(
    messages: list, model_name: str = constants.LOCAL_MODELS[0], temperature: float = 0.8
) -> str:
    """
    Local Chat Completion Function
    """
    client = Client(host="http://127.0.0.1:11434")

    chat_completion = client.chat(
        stream=False,
        model=model_name,
        messages=messages,
        options={"temperature": temperature},
    )
    assistant_answer: str | None = chat_completion.message.content
    if not assistant_answer:
        assistant_answer = constants.NOT_FOUND
    return assistant_answer