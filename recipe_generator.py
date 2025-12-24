import ollama
import json

SYSTEM_PROMPT = """
You are a professional chef AI.
Extract a clean recipe from noisy video data.

Rules:
- Use only ingredients mentioned or seen
- Infer steps logically
- Output STRICT JSON
"""

def generate_recipe(context):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(context)}
        ]
    )

    content = response["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "title": "Unknown",
            "ingredients": [],
            "steps": [content]
        }
