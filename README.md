#  Agentic Scam Honeypot - GUVI Hackathon

An AI-powered honeypot system featuring **Sara** - a natural-sounding Indian woman who engages with scammers, extracts intelligence, and sounds completely authentic.

## 👩 Meet Sara - The AI Agent

Sara is NOT a robot. She's a 40-50 year old Indian school teacher who:
- Speaks natural Hinglish (Hindi-English mix)
- Sounds confused and hesitant
- Asks innocent questions that extract information
- NEVER reveals she knows it's a scam
- Acts like a real victim on a phone call

**Example Conversation:**
```
📞 Scammer: "Madam, aapka account block hone wala hai"
👩 Sara: "Kya? Konsa account? Main confused hoon"
📞 Scammer: "State Bank account. KYC pending hai"
👩 Sara: "Achha... toh kya karna hoga?"
```

**Read more:** [SARA_PERSONA.md](./SARA_PERSONA.md)

---

##  Features

 **Intelligent Scam Detection** - Multi-pattern analysis with confidence scoring
 **Sara - AI Agent** - Natural Indian persona that sounds completely real
 **Hinglish Conversations** - Natural Hindi-English mix like real Indians speak
 **Intelligence Extraction** - Automatically extracts bank accounts, UPI IDs, phone numbers, links
 **Multi-turn Conversations** - Maintains context across conversation history
 **Human-like Behavior** - Confused, hesitant, with environmental context (school, network issues)
 **Automatic Reporting** - Sends final intelligence to GUVI evaluation endpoint
 **REST API** - Easy integration with FastAPI
 **Secure Authentication** - API key protection

## Architecture

```
┌─────────────────┐
│  Scammer Message│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Scam Detection  │ ◄── Pattern matching + Context analysis
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  AI Agent       │ ◄── Claude Sonnet 4 generates response
│ (Claude)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│Intelligence     │ ◄── Extract data from messages
│Extraction       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Send to GUVI    │ ◄── Final callback when done
└─────────────────┘
### Python Example

```python
import requests

url = "http://localhost:8000/api/detect"
headers = {
    "x-api-key": "HONEY-POT-SECURE-KEY-2024-GUVI-HACK",
    "Content-Type": "application/json"
}

payload = {
    "sessionId": "test-123",
    "message": {
        "sender": "scammer",
        "text": "Your account is blocked. Call +919876543210 immediately",
        "timestamp": 1770005528731
    },
    "conversationHistory": [],
    "metadata": {
        "channel": "SMS",
        "language": "English",
        "locale": "IN"
    }
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

##  How It Works

### 1. Scam Detection
The system uses multiple pattern categories:
- **Urgency**: "immediately", "urgent", "today"
- **Account Threats**: "blocked", "suspended", "freeze"
- **Verification Requests**: "verify", "confirm", "validate"
- **Payment Related**: "UPI", "bank account", "OTP", "CVV"
- **Prize/Reward**: "won", "prize", "lottery"
- **Authority Impersonation**: "bank", "police", "government"

### 2. AI Agent Behavior
Claude AI is prompted to:
- Act as a confused, concerned victim
- Ask questions that extract information
- Show hesitation and worry
- Never reveal detection
- Make scammers work to convince them

### 3. Intelligence Extraction
Automatically extracts:
- Bank account numbers
- UPI IDs
- Phone numbers
- Phishing links
- Suspicious keywords

### 4. Automatic Callback
After sufficient engagement (10+ messages or critical info gathered), the system automatically sends results to:
```
POST https://hackathon.guvi.in/api/updateHoneyPotFinalResult


##  Evaluation Criteria Coverage

 **Scam Detection Accuracy**: Multi-pattern analysis with confidence scoring
 **Quality of Agentic Engagement**: Claude AI generates contextual responses
 **Intelligence Extraction**: Regex-based extraction of all required data types
 **API Stability**: FastAPI with error handling and logging
 **Ethical Behavior**: No impersonation, no illegal instructions, responsible engagement




##  Scam Categories Detected

1. **Bank Fraud** - Account blocking threats
2. **UPI Fraud** - Payment redirection scams
3. **Phishing** - Fake links and credentials theft
4. **OTP Scams** - One-time password requests
5. **Prize/Lottery** - Fake rewards
6. **Authority Impersonation** - Fake government/bank officials
7. **Urgency Tactics** - Time pressure scams



