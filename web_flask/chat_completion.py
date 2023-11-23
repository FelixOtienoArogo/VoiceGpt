from openai import OpenAI
import json
client = OpenAI()

def chat_completion(search_text):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON that has only one key."},
        {"role": "user", "content": search_text}
        ]
    )
    data = json.loads(response.choices[0].message.content)
    return list(data.values())[0]
