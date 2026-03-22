from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    role: str
    message: str

@app.get("/")
def home():
    return {"message": "Chatbot API is running 🚀"}

@app.post("/chat")
def chat(request: ChatRequest):
    reply = get_response(request.role, request.message)
    return {"response": reply}