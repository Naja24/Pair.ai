import requests

def generate_response(user_msg, emotion):
    prompt = f"You are a {emotion} AI. Respond accordingly."

    response = requests.post("http://localhost:11434/api/chat", json={
        "model": "mistral",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_msg}
        ]
    })

    return response.json()['message']['content']
