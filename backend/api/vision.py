import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_chart(image_base64, uid):
    response = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this chart and provide trade setup with Pine Script. Include pattern, entry, SL, TP."},
                    {"type": "image_url", "image_url": {"url": image_base64}}
                ]
            }
        ],
        max_tokens=1500
    )
    return {"summary": response.choices[0].message.content}