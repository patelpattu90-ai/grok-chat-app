import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROK_API_KEY")
BASE_URL = "https://api.x.ai/v1/chat/completions"

def chat_with_grok(messages, temperature=0.2):
    if not API_KEY:
        return "ERROR: GROK_API_KEY not set"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-beta",
        "messages": messages,
        "temperature": temperature,
        "stream": False
    }

    r = requests.post(BASE_URL, headers=headers, json=payload, timeout=30)
    if r.status_code != 200:
        return f"ERROR {r.status_code}: {r.text}"

    return r.json()["choices"][0]["message"]["content"]

