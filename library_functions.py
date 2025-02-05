"""
Functions Library
"""

import os
import nest_asyncio
import library_constants

from openai import OpenAI
from dotenv import load_dotenv


def get_api_key() -> str:
    """
    Get API Key Function
    """

    loaded = load_dotenv()

    if loaded == False:
        print("Loading '.env' file failed!")
        exit()

    api_key = os.environ.get(key=library_constants.API_KEY_NAME)

    return api_key


def init() -> None:
    """
    Initialize Function
    """

    nest_asyncio.apply()


def get_response(
    api_key: str, model_name: str, query: str, temperature: float = 0.8
) -> str:
    """
    Get Response Function
    """

    messages = []

    system_message = {"role": "system", "content": library_constants.SYSTEM_PROMPT}
    messages.append(system_message)

    user_message = {"role": "user", "content": query}
    messages.append(user_message)

    client = OpenAI(api_key=api_key, base_url=library_constants.BASE_URL)

    response = client.chat.completions.create(
        stream=False,
        model=model_name,
        messages=messages,
        temperature=temperature,
    )

    result: str = response.choices[0].message.content.strip()

    return result


if __name__ == "__main__":
    print("This file is a library file! So, you cannot run this file directly...")
