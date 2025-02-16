# LocalAi

چت بات شخصی استفاده از مدهای لوکال با استفاده از ollama و مدل های آنلاین Groq. برای استفاده از Groq نیاز به تغییر آی پی دارید.

برای اجرا باید دستور `streamlit run ./streamlit_app.py` را در ترمینال اجرا کنید
## Setup Environment

- python -m venv .venv
- .\\.venv\Scripts\activate
- pip list

<br>

- python -m pip install -U pip
- python -m pip install -U groq
- python -m pip install -U python-dotenv
- python -m pip install -U ollama
- 
<br>

- python -m pip install -U streamlit
- pip list

Write / Edit / Run the Source Code(s)!

- deactivate

## Create .env File (For Saving Passwords / API Keys / Access Tokens / ...)

- In the root of project, create a file, with the name of '.env', and write key name(s) and value:
    - GROQ_API_KEY="..."
