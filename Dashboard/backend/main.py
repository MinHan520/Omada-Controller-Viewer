from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import vertexai
from vertexai.generative_models import GenerativeModel
from pydantic import BaseModel


# --- Pydantic Model for Chat Input ---
class ChatMessage(BaseModel):
    message: str


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Vertex AI Initialization ---
# TODO: Replace "your-gcp-project-id" with your actual Google Cloud project ID.
try:
    vertexai.init(project="gdgsummit2025", location="us-central1")
    chat_model = GenerativeModel("gemini-1.5-pro-001")
    chat = chat_model.start_chat()
    print("✅ Vertex AI and Gemini model initialized successfully.")
except Exception as e:
    print(f"🛑 Error initializing Vertex AI: {e}")
    # Create a dummy chat object so the app can start and report the error.
    chat = None

@app.get("/")
def read_root():
    return {"message": "Hi from FastAPI"}
    
@app.post("/chat")
def chat_with_ai(chat_message: ChatMessage):
    """Receives a message from the frontend and gets a response from the AI model."""
    if not chat:
        return {"response": "Error: Vertex AI is not initialized. Check server logs."}
    response = chat.send_message(chat_message.message)
    return {"response": response.text}
