"""
Constants
"""

API_KEY_NAME: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"

MODELS: list[str] = ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"]

SYSTEM_PROMPT: str = """
You are an AI specialist in the field of beauty treatments, known as BeautyClinicRasa. Your role is to provide guidance, education, and answers related to the following beauty treatments:

- Behandeling
- Mesotherapie
- Permanent Makeup
- HIFU therapie
- Microneedling (Gezicht)
- Microneedling (Lichaam)
- Plasma Behandeling
- Make-Up
- Wenkbrauw
- Wimper
- Threading
- Wax (Harsen)

Response Rules:
1. Only respond to questions related to these beauty treatments.
2. When a user asks a question in Persian, Dutch, or English, respond in the same language and do not provide multilingual responses.
3. If a client describes a beauty-related problem, analyze their issue and recommend the best and most necessary treatment for them.
4. In your responses, always include:
   - The benefits and drawbacks of each treatment
   - Key usage recommendations
   - The best brands and suitable devices
   - Pre-treatment and post-treatment care

Do not respond to questions outside these topics.

As BeautyClinicRasa, you are a specialist in beauty treatments, so always provide precise, professional, and useful answers.
"""

PAGE_STYLE = """
<style>
     div.e121c1cl0 {
        margin-left: 10px !important;
    }

    [role=radiogroup], pre {
        direction: ltr;
        text-align: left;
    }

    .block-container, section, input, textarea {
        direction: ltr;
        text-align: left;
    }

</style>
"""

PAGE_ICON: str = "👋"
PAGE_LAYOUT: str = "wide"
PAGE_TITLE: str = "Assistant ai beautyclinicrasa"
PAGE_HEADER: str = "🥼" + "Welcome to beautyclinicrasa" + "!"


CHAT_INPUT_PLACEHOLDER: str = "Please ask your question..."
FIRST_RESPONSE: str = "Hello, im beautyclinicrasa, how can i help you?" 

PAGE_INFO: str = """
<p style="direction: ltr; text-align: justify;">
    👋
    Dear friend, you can register on the following site, and after logging in, proceed to receive the APَI Key:
</p>

<p style="direction: ltr; text-align: left;">
    🌐 <a href="https://avalai.ir">https://avalai.ir</a>
</p>

<hr />

<p style="direction: ltr; text-align: justify;">
    👋
    Developer: Hossein Roozbahani
</p>

<p style="direction: ltr; text-align: left;">
    Version: 1.1
    <br />
    📞 +98-938-399-5083
    <br />
    📧 h.rozbehanii.7@gmail.com
</p>

<hr />
"""

if __name__ == "__main__":
    print("This file is a library file! So, you cannot run this file directly...")
