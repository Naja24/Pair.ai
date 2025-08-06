# server/app/api/routes.py

from fastapi import APIRouter, WebSocket, Request
from packages.ai_engine.utils.sentiment import detect_sentiment
from packages.ai_engine.prompts.default_prompt import generate_prompt

router = APIRouter()

# 1. WebSocket Endpoint (Live Echo for now)
@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")

# 2. HTTP POST Endpoint for Sentiment Analysis
@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    sentiment = detect_sentiment(user_message)
    prompt = f"The user is feeling {sentiment}. Respond accordingly.\nUser: {user_message}"

    # Mock LLM response (replace later)
    response = f"[Mock LLM Reply] (Sentiment: {sentiment})"

    return {"response": response, "sentiment": sentiment}
