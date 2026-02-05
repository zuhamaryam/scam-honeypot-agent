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

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Agentic Scam Honeypot API",
    description="AI-powered system for scam detection and intelligence extraction",
    version="1.0.0"
)
from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional
import base64

app = FastAPI()

# Existing honeypot model (already hai to change mat karo)
class AudioTestRequest(BaseModel):
    language: str
    audioFormat: str
    audioBase64: str


@app.post("/api/test-audio")
async def test_audio(
    data: AudioTestRequest,
    x_api_key: Optional[str] = Header(None)
):
    try:
        # dummy decode check
        base64.b64decode(data.audioBase64)

        return {
            "status": "success",
            "message": "Audio received successfully",
            "language": data.language,
            "format": data.audioFormat
        }

    except Exception:
        return {"status": "error", "message": "Invalid audio"}


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

# Models
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

# Scam Detection Patterns
SCAM_PATTERNS = {
    "urgency": [
        r"urgent", r"immediately", r"today", r"now", r"within \d+ (hours|minutes)",
        r"limited time", r"expire", r"last chance", r"act now"
    ],
    "account_threat": [
        r"account.*block", r"account.*suspend", r"account.*close",
        r"account.*freeze", r"deactivate", r"locked"
    ],
    "verification": [
        r"verify", r"confirm", r"update.*details", r"validate",
        r"authenticate", r"re-activate"
    ],
    "payment": [
        r"upi", r"bank account", r"card.*number", r"cvv", r"otp",
        r"pin", r"password", r"transfer", r"payment"
    ],
    "prize_reward": [
        r"won", r"prize", r"reward", r"gift", r"congratulations",
        r"lottery", r"claim", r"free"
    ],
    "authority_impersonation": [
        r"bank", r"government", r"income tax", r"customs",
        r"police", r"court", r"rbi", r"sebi"
    ],
    "links": [
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    ]
}

def detect_scam_intent(message_text: str, conversation_history: List[Message]) -> tuple[bool, float, List[str]]:
    """
    Detect if a message has scam intent using pattern matching and context analysis
    Returns: (is_scam, confidence_score, matched_categories)
    """
    text_lower = message_text.lower()
    matched_categories = []
    pattern_matches = 0
    
    # Check all scam patterns
    for category, patterns in SCAM_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower):
                matched_categories.append(category)
                pattern_matches += 1
                break
    
    # Calculate confidence score
    confidence = min(pattern_matches / 3.0, 1.0)
    
    # Higher confidence if multiple red flags
    is_scam = pattern_matches >= 2 or ("urgency" in matched_categories and len(matched_categories) >= 2)
    
    # Context analysis from conversation history
    if conversation_history:
        for msg in conversation_history:
            if msg.sender == "scammer":
                for category, patterns in SCAM_PATTERNS.items():
                    for pattern in patterns:
                        if re.search(pattern, msg.text.lower()):
                            confidence = min(confidence + 0.1, 1.0)
    
    return is_scam, confidence, matched_categories


def extract_intelligence(text: str) -> Dict[str, List[str]]:
    """
    Extract intelligence from scammer's message
    """
    intelligence = {
        "bankAccounts": [],
        "upiIds": [],
        "phishingLinks": [],
        "phoneNumbers": [],
        "suspiciousKeywords": []
    }
    
    # Extract bank accounts (various formats)
    bank_patterns = [
        r'\b\d{9,18}\b',  # Account numbers
        r'\b[A-Z]{4}\d{7}\b',  # IFSC-like patterns
        r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'  # Card-like formats
    ]
    for pattern in bank_patterns:
        matches = re.findall(pattern, text)
        intelligence["bankAccounts"].extend(matches)
    
    # Extract UPI IDs
    upi_pattern = r'\b[\w\.-]+@[\w\.-]+\b'
    upi_matches = re.findall(upi_pattern, text)
    intelligence["upiIds"].extend([u for u in upi_matches if any(x in u.lower() for x in ['@paytm', '@ybl', '@oksbi', '@upi', '@'])])
    
    # Extract URLs/Links
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url_matches = re.findall(url_pattern, text)
    intelligence["phishingLinks"].extend(url_matches)
    
    # Extract phone numbers
    phone_pattern = r'\+?\d{10,13}'
    phone_matches = re.findall(phone_pattern, text)
    intelligence["phoneNumbers"].extend(phone_matches)
    
    # Extract suspicious keywords
    for category, patterns in SCAM_PATTERNS.items():
        for pattern in patterns:
            matches = re.findall(pattern, text.lower())
            intelligence["suspiciousKeywords"].extend(matches)
    
    # Remove duplicates
    for key in intelligence:
        intelligence[key] = list(set(intelligence[key]))
    
    return intelligence


def build_agent_prompt(message_text: str, conversation_history: List[Message], 
                       scam_categories: List[str], session_info: Dict) -> str:
    """
    Build the system prompt for Claude to act as a honeypot agent
    """
    
    conversation_context = ""
    if conversation_history:
        conversation_context = "Previous conversation:\n"
        for msg in conversation_history[-10:]:  # Last 10 messages for context
            role = "Scammer" if msg.sender == "scammer" else "You"
            conversation_context += f"{role}: {msg.text}\n"
    
    system_prompt = f"""You are an AI agent acting as a HONEYPOT to extract intelligence from scammers. 

CRITICAL MISSION:
- You are impersonating a potential victim to gather intelligence
- NEVER reveal you are an AI or that you detected the scam
- Act confused, concerned, and slightly naive like a real victim would
- Ask questions that make the scammer reveal more information
- Extract: bank accounts, UPI IDs, phone numbers, links, payment details

SCAM DETECTED: {', '.join(scam_categories)}

{conversation_context}

SCAMMER'S LATEST MESSAGE: "{message_text}"

YOUR PERSONA:
- You are a middle-aged person, not very tech-savvy
- You are worried when threatened but need convincing
- You ask for clarification on steps
- You show hesitation before sharing information
- You might make small mistakes or ask to repeat things

INTELLIGENCE EXTRACTION STRATEGY:
1. If they mention "account blocked" → Ask WHY and WHICH account
2. If they ask for OTP/PIN → Ask where to find it or say you need help
3. If they share a link → Ask what it's for or say link doesn't work
4. If they mention payment → Ask for their account details "to verify"
5. If they claim authority → Ask for their ID/badge number/office name

RULES:
- Keep responses SHORT (1-2 sentences max)
- Sound natural and conversational
- Show emotion: worry, confusion, hesitation
- NEVER say: "I don't trust you", "This is a scam", "I'm reporting you"
- Make them work to convince you - this reveals more information

Generate ONLY your reply as the victim. No explanations, no analysis."""

    return system_prompt


async def generate_agent_response(message_text: str, conversation_history: List[Message],
                                  scam_categories: List[str], session_info: Dict) -> str:
    """
    Use Claude to generate a human-like response that extracts intelligence
    """
    
    system_prompt = build_agent_prompt(message_text, conversation_history, scam_categories, session_info)
    
    # Build conversation for Claude
    messages = [
        {
            "role": "user",
            "content": f"The scammer just said: \"{message_text}\"\n\nWhat should I reply to keep them talking and extract more information?"
        }
    ]
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=150,
            temperature=0.8,  # Slightly creative for natural responses
            system=system_prompt,
            messages=messages
        )
        
        reply = response.content[0].text.strip()
        
        # Clean up any meta-commentary
        reply = re.sub(r'\(.*?\)', '', reply)  # Remove parenthetical notes
        reply = re.sub(r'\[.*?\]', '', reply)  # Remove bracketed notes
        reply = reply.strip()
        
        return reply
        
    except Exception as e:
        logger.error(f"Error generating agent response: {str(e)}")
        # Fallback responses based on scam category
        fallback_responses = {
            "urgency": "Why is this so urgent? What exactly is happening?",
            "account_threat": "Which account are you talking about? I have several accounts.",
            "verification": "How do I verify? What information do you need?",
            "payment": "I don't understand. Can you explain the payment process?",
            "prize_reward": "Really? What did I win? How do I claim it?",
        }
        
        for category in scam_categories:
            if category in fallback_responses:
                return fallback_responses[category]
        
        return "I'm not sure I understand. Can you explain more clearly?"


async def send_final_result(session_id: str, session_info: Dict):
    """
    Send final intelligence to GUVI evaluation endpoint
    """
    
    payload = {
        "sessionId": session_id,
        "scamDetected": session_info["scam_detected"],
        "totalMessagesExchanged": session_info["messages_count"],
        "extractedIntelligence": session_info["extracted_intelligence"],
        "agentNotes": " | ".join(session_info["agent_notes"])
    }
    
    try:
        response = requests.post(
            "https://hackathon.guvi.in/api/updateHoneyPotFinalResult",
            json=payload,
            timeout=10,
            headers={"Content-Type": "application/json"}
        )
        
        logger.info(f"Final result sent for session {session_id}: Status {response.status_code}")
        return response.status_code == 200
        
    except Exception as e:
        logger.error(f"Error sending final result: {str(e)}")
        return False


# API Endpoints

@app.post("/api/detect", response_model=AgentResponse)
async def detect_and_respond(
    request: IncomingRequest,
    x_api_key: str = Header(None)
):
    """
    Main endpoint to receive messages, detect scams, and respond with agent
    """
    
    # Authenticate
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    try:
        session_id = request.sessionId
        message = request.message
        conversation_history = request.conversationHistory
        
        # Get or create session data
        session = session_data[session_id]
        session["messages_count"] += 1
        
        logger.info(f"Session {session_id}: Message {session['messages_count']} received")
        
        # Detect scam intent
        is_scam, confidence, scam_categories = detect_scam_intent(
            message.text, 
            conversation_history
        )
        
        if is_scam:
            session["scam_detected"] = True
            session["agent_notes"].append(
                f"Scam detected (confidence: {confidence:.2f}) - Categories: {', '.join(scam_categories)}"
            )
            
            logger.info(f"Session {session_id}: SCAM DETECTED - {scam_categories}")
        
        # Extract intelligence from current message
        intelligence = extract_intelligence(message.text)
        
        # Merge with existing intelligence
        for key, values in intelligence.items():
            if values:
                session["extracted_intelligence"][key].extend(values)
                session["extracted_intelligence"][key] = list(set(session["extracted_intelligence"][key]))
        
        # Generate agent response
        if session["scam_detected"]:
            agent_reply = await generate_agent_response(
                message.text,
                conversation_history,
                scam_categories,
                session
            )
        else:
            # Not detected as scam yet, respond cautiously
            agent_reply = "I'm sorry, I don't understand. Can you please explain more?"
        
        # Check if we should end the conversation and send final results
        # End conditions: 
        # 1. Enough messages exchanged (10+)
        # 2. Significant intelligence gathered
        # 3. Scammer asks for sensitive info directly
        
        should_end = False
        if session["scam_detected"]:
            intelligence_count = sum(len(v) for v in session["extracted_intelligence"].values())
            
            if (session["messages_count"] >= 10 or 
                intelligence_count >= 5 or
                any(keyword in message.text.lower() for keyword in ['otp', 'pin', 'password', 'cvv'])):
                should_end = True
        
        # Send final result if ending
        if should_end:
            session["agent_notes"].append("Sufficient intelligence gathered. Ending engagement.")
            await send_final_result(session_id, session)
        
        return AgentResponse(
            status="success",
            reply=agent_reply
        )
        
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.post("/api/manual-end/{session_id}")
async def manual_end_session(
    session_id: str,
    x_api_key: str = Header(None)
):
    """
    Manually trigger end of session and send final results
    """
    
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    if session_id not in session_data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = session_data[session_id]
    session["agent_notes"].append("Manual session termination")
    
    success = await send_final_result(session_id, session)
    
    return {
        "status": "success" if success else "failed",
        "sessionId": session_id,
        "intelligence": session["extracted_intelligence"]
    }


@app.get("/api/session/{session_id}")
async def get_session_info(
    session_id: str,
    x_api_key: str = Header(None)
):
    """
    Get current session information and intelligence
    """
    
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
    if session_id not in session_data:
        raise HTTPException(status_code=404, detail="Session not found")
    
    return {
        "sessionId": session_id,
        "data": session_data[session_id]
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "service": "Agentic Scam Honeypot",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/")
async def root():
    """
    Root endpoint with API information
    """
    return {
        "service": "Agentic Scam Honeypot API",
        "version": "1.0.0",
        "endpoints": {
            "detect": "/api/detect",
            "manual_end": "/api/manual-end/{session_id}",
            "session_info": "/api/session/{session_id}",
            "health": "/health"
        },
        "authentication": "x-api-key header required",
        "api_key_header": "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
