import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROK_API_KEY")
BASE_URL = "https://api.x.ai/v1/chat/completions"

def chat_with_grok(messages, temperature=0.2):
    if not API_KEY:
        return "ERROR: GROK_API_KEY not found"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-2-latest",
        "messages": messages,
        "temperature": temperature
    }

    r = requests.post(BASE_URL, headers=headers, json=payload)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

