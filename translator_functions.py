"""
Translator Functions
"""

import re
from groq import Groq
from dotenv import load_dotenv
import translator_constants as constants
from ollama import Client

def read_text_file(pathfile: str) -> str:
    """
    Read Text File
    """

    with open(file=pathfile, mode="rt", encoding="utf-8") as file:
        result: str = file.read()
        file.close()

    return result


def normalize_text(text: str) -> str:
    """
    Normalize Text Function
    """

    result: str = text

    while "  " in result:
        result = result.replace("  ", " ")

    result = result.replace("\n", "")
    result = result.replace("\r", "")

    return result


def get_sentences(text: str) -> list[str]:
    """
    Get Sentences Function
    """

    pattern = r"[.!?]+"

    parts = re.split(pattern=pattern, string=text)

    sentences: list[str] = []

    for part in parts:
        if not part:
            continue

        part = part.strip()

        if not part:
            continue

        sentences.append(part)

    return sentences


def get_paragraphs(text: str) -> list[str]:
    """
    Get Paragraphs Function
    """

    paragraphs = text.split("\n\n")

    return paragraphs


def groq_translate(
    text: str,
    model_name: str = "llama-3.1-8b-instant",
    temperature: float = 0.0,
) -> str:
    """
    Online Translate Function, Groq model is used for translation.
    """

    load_dotenv()
    client = Groq()

    messages = []

    messages.append(constants.SYSTEM_MESSAGE)

    user_message = {"role": "user", "content": text}
    messages.append(user_message)

    chat_completion = client.chat.completions.create(
        stream=False,
        model=model_name,
        messages=messages,
        temperature=temperature,
    )

    assistant_answer: str | None = chat_completion.choices[0].message.content

    if not assistant_answer:
        assistant_answer = constants.UNSUCCESS_ANSWER

    return assistant_answer

def local_translate(
    text: str,
    model_name: str = "llama-3.1:latest",
    temperature: float = 0.0,
) -> str:
    """
    offline Translate Function. Ollama model is used for translation.
    """

    messages = []

    messages.append(constants.SYSTEM_MESSAGE)

    user_message = {"role": "user", "content": text}
    messages.append(user_message)


    client = Client(host="http://127.0.0.1:11434")

    chat_completion = client.chat(
        stream=False,
        model=model_name,
        messages=messages,
        options={"temperature": temperature},
    )

    assistant_answer: str | None = chat_completion.message.content

    if not assistant_answer:
        assistant_answer = constants.UNSUCCESS_ANSWER

    return assistant_answer



if __name__ == "__main__":
    print("You must run the translator.py file!")