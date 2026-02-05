"""
Agentic Honey-Pot for Scam Detection & Intelligence Extraction
GUVI Hackathon Submission
"""

from fastapi import FastAPI, HTTPException, Header, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
import anthropic
import re
import json
import requests
from datetime import datetime
import logging
import os
from collections import defaultdict
import base64

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Agentic Scam Honeypot API",
    description="AI-powered system for scam detection and intelligence extraction",
    version="1.0.0"
)

# API Key for authentication
API_KEY = "HONEY-POT-SECURE-KEY-2024-GUVI-HACK"

# Anthropic Claude client
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

# Session storage (in production, use Redis/Database)
session_data = defaultdict(lambda: {
    "scam_detected": False,
    "messages_count": 0,
    "extracted_intelligence": {
        "bankAccounts": [],
        "upiIds": [],
        "phishingLinks": [],
        "phoneNumbers": [],
        "suspiciousKeywords": []
    },
    "agent_notes": []
})

# --- Models ---

class AudioTestRequest(BaseModel):
    sessionId: str  # ✅ Added sessionId here
    language: str
    audioFormat: str
    audioBase64: str

class Message(BaseModel):
    sender: str
    text: str
    timestamp: int

class Metadata(BaseModel):
    channel: Optional[str] = "SMS"
    language: Optional[str] = "English"
    locale: Optional[str] = "IN"

class IncomingRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[Message] = []
    metadata: Optional[Metadata] = Metadata()

class AgentResponse(BaseModel):
    status: str
    reply: str

# --- Scam Detection Patterns ---
SCAM_PATTERNS = {
    "urgency": [r"urgent", r"immediately", r"today", r"now", r"within \d+ (hours|minutes)", r"limited time", r"expire", r"last chance", r"act now"],
    "account_threat": [r"account.*block", r"account.*suspend", r"account.*close", r"account.*freeze", r"deactivate", r"locked"],
    "verification": [r"verify", r"confirm", r"update.*details", r"validate", r"authenticate", r"re-activate"],
    "payment": [r"upi", r"bank account", r"card.*number", r"cvv", r"otp", r"pin", r"password", r"transfer", r"payment"],
    "prize_reward": [r"won", r"prize", r"reward", r"gift", r"congratulations", r"lottery", r"claim", r"free"],
    "authority_impersonation": [r"bank", r"government", r"income tax", r"customs", r"police", r"court", r"rbi", r"sebi"],
    "links": [r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"]
}

# --- /api/test-audio endpoint ---
@app.post("/api/test-audio")
async def test_audio(
    data: AudioTestRequest,
    x_api_key: Optional[str] = Header(None)
):
    # Authenticate API Key
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        # Check if audio is valid base64
        base64.b64decode(data.audioBase64)
        return {
            "status": "success",
            "message": "Audio received successfully",
            "sessionId": data.sessionId,
            "language": data.language,
            "format": data.audioFormat
        }
    except Exception:
        return {"status": "error", "message": "Invalid audio", "sessionId": data.sessionId}

# --- Rest of your honeypot scam detection endpoints ---
# (Keep all your existing /api/detect, /api/manual-end, /api/session, health, root)
# ... <copy your existing code from here> ...

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from fastapi import FastAPI, File, UploadFile, HTTPException, Header
from typing import Optional
import os

app = FastAPI()

# API Key for authentication
API_KEY = "HONEY-POT-SECURE-KEY-2024-GUVI-HACK"

# Folder to temporarily save uploaded audio (optional)
UPLOAD_FOLDER = "uploaded_audios"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/api/upload-audio")
async def upload_audio(
    sessionId: str,
    language: str,
    audioFile: UploadFile = File(...),
    x_api_key: Optional[str] = Header(None)
):
    # Authenticate API Key
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Check if uploaded file is audio
    if not audioFile.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an audio file")

    try:
        # Save the uploaded file temporarily (optional)
        file_location = os.path.join(UPLOAD_FOLDER, f"{sessionId}_{audioFile.filename}")
        with open(file_location, "wb") as f:
            f.write(await audioFile.read())

        # You can now process this file with your AI or scam detection logic
        return {
            "status": "success",
            "message": f"Audio received successfully: {audioFile.filename}",
            "sessionId": sessionId,
            "language": language,
            "filePath": file_location
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process audio: {str(e)}")


