import json
import os

import dotenv
from openai import OpenAI

dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env', '.env-chatgpt'))
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(json.dumps(json.loads(completion.choices[0].message.content), indent=2, ensure_ascii=False))