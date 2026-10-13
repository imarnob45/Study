import os
import sys

try:
    from openai import OpenAI
except ModuleNotFoundError:
    print("The 'openai' package is missing. Install it with: python -m pip install -r requirements.txt")
    sys.exit(1)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Set the OPENAI_API_KEY environment variable before running this script.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        input="Heyy? How are you doing?",
        model="gpt-5",
    )
except Exception as exc:
    print(f"OpenAI request failed: {exc}")
    sys.exit(1)

print(response.output_text)