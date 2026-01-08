import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "qwen/qwen3-32b"


def chat_with_groq(messages, temperature=0.2):
    if not API_KEY:
        return "❌ ERROR: GROQ_API_KEY not set"

    # Ensure valid message format
    if not isinstance(messages, list):
        return "❌ ERROR: messages must be a list"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": temperature
    }

    try:
        r = requests.post(BASE_URL, headers=headers, json=payload, timeout=30)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"]

    except requests.exceptions.HTTPError:
        return f"❌ HTTP Error {r.status_code}: {r.text}"

    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {str(e)}"

    except KeyError:
        return f"❌ Invalid response format: {r.text}"


