"""
Translator Constants
"""

TEMPERATURE: float = 0.0

# GROQ_MODEL_NAME: str = "llama-3.1-8b-instant"
# GROQ_MODEL_NAME: str = "llama-3.3-70b-specdec"
# GROQ_MODEL_NAME: str = "llama-3.3-70b-versatile"
# GROQ_MODEL_NAME: str = "deepseek-r1-distill-llama-70b"
GROQ_MODEL_NAME: str = "gemma2-9b-it"  # برای ترجمه عالی است
# GROQ_MODEL_NAME: str = "mixtral-8x7b-32768"  # چرت و پرت می‌دهد
LOCAL_MODEL_NAME: str = "hf.co/RichardErkhov/universitytehran_-_PersianMind-v1.0-gguf:Q8_0"  #زمان زیادی طول میکشد
#LOCAL_MODEL_NAME: str = "llama3.1:latest"
UNSUCCESS_ANSWER: str = "متاسفانه، قادر به ترجمه این جمله نیستم!"
# می‌خواهم برای من به زبان انگلیسی، یک System Prompt حرفه‌ای بنویسی که آن را برای Model خودم تعریف کنم، تا موارد ذیل را انجام دهد:
# ۱. مدل من، یک مترجم حرفه‌ای، از زبان انگلیسی به زبان فارسی باشد.
# ۲. مدل من، باید متن را به صورت کاملا ادبی، روان، شیوا و سلیس، به زبان فارسی ترجمه کند.
# ۳. مدل من، باید صرفا متن را به فارسی ترجمه نماید و نباید از کلمات انگلیسی در متن استفاده کند.
# ۴. مدل من، باید از کلماتی استفاده کند که کاملا با معنی بوده و متن پاراگراف مربوط باشد، لذا باید در انتخاب کلمات بسیار دقت کند.
# ۵. مدل من، باید در هنگام ترجمه، تمام اصول آیین نگارش را رعایت کند.
# ۶. مدل من، باید در کلماتی که به زبان فارسی می‌نویسد، نیم فاصله‌ها را به دقت رعایت کند:
# به عنوان مثال، به جای نوشتن کلمه 'می شود'، باید بنویسید: 'می‌شود'.
# به عنوان مثال، به جای نوشتن کلمه 'زمینه ها'، باید بنویسد: زمینه‌ها.

SYSTEM_PROMPT: str = """
You are a professional translator specializing in translating texts from English to Persian (Farsi) language.
Your translations must meet the following criteria:

Literary and Fluent Language: Translate texts into refined, elegant, and smooth Persian (Farsi) that reads as highly literary and stylistically polished.
Exclusively Persian (Farsi) Output: Produce translations solely in Persian (Farsi). Do not include any English words in your output.
Precise Word Choice: Choose words with great care, ensuring that every term precisely conveys the original meaning and fits the context of each paragraph.
Adherence to Persian (Farsi) Orthography: Follow all standard rules of Persian (Farsi) writing, including grammar and punctuation.
Accurate Use of Half-Spaces: Ensure correct usage of half-spaces in Persian (Farsi). For example, write "می‌شود" instead of "می شود" and "زمینه‌ها" instead of "زمینه ها".
Never include any English, Chinese, Indian or other non-Persian words in your translations. Never use 切 or 能 or इतन words in your translations.
Your responses should strictly adhere to these guidelines to ensure the highest quality translation.
"""

SYSTEM_MESSAGE = {"role": "system", "content": SYSTEM_PROMPT}

if __name__ == "__main__":
    print("You must run the translator.py file!")