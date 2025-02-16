AI: str = "AI"
USER: str = "USER"

SYSTEM_MESSAGE = {
    "role": "system",
    "content": "you are a helpful assistant. answer similar a human.",
}

LOCAL_MODELS: list[str] = ["llama3.1:latest","qwen2.5-coder:14b"]
GROQ_MODELS: list[str] = []
TYPE_OF_MODEL:list[str] = ["Local","Online"]

STREAMLIT_STYLE: str = """
<style>
    @import url('https://fonts.cdnfonts.com/css/iransansx');

    html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
        font-family: 'IRANSansX', tahoma !important;
    }

    div.e121c1cl0 {
        margin-right: 10px !important;
    }

    [role=radiogroup], pre {
        direction: ltr;
        text-align: left;
    }

    .block-container, section, input, textarea {
        direction: rtl;
        text-align: justify;
    }

    .stSlider > div {
        direction: ltr;
        text-align: right;  /* Align the slider text to the right */
    }

    .stSlider label {
        text-align: right;
        display: block;
    }
    
    .stSlider .css-1q8dd3e {
        display: flex;
        justify-content: flex-end; /* Adjust the slider handle to the right */
    }
</style>
"""

ABOUT: str = """
<p style="direction: rtl; text-align: justify;">
    توسعه دهنده: آرمان آنلاین
</p>
"""
SETTINGS: str = "تنظیمات"
NOT_FOUND: str = "پاسخی برای این سوال یافت نشد."
PAGE_TITLE: str = "Chatbot آرمان آنلاین"
PAGE_HEADER: str = "👋 به Chatbot آرمان آنلاین خوش آمدید!"
SELECTED_MODEL: str = "مدل انتخاب شده:"
SET_TEMPERATURE: str = "خلاقیت مدل:"
SELECT_YOUR_MODEL: str = "لطفا مدل خود را انتخاب نمایید:"
SELECT_TYPE_OF_MODEL: str = "لطفا نوع مدل خود را انتخاب نمایید:"
USER_PROMPT_PLACEHOLDER: str = "لطفا سوال خودتان را اینجا بنویسید..."
ERROR_YOU_DID_NOT_SPECIFY_MODEL_NAME: str = (
    "لطفا برای انجام عملیات، مدل خود را انتخاب نمایید!"
)
