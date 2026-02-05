# 🍯 Agentic Scam Honeypot - GUVI Hackathon

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
👩 Sara: "Kya? Kaunsa account? Main confused hoon"
📞 Scammer: "State Bank account. KYC pending hai"
👩 Sara: "Achha... toh kya karna hoga?"
```

**Read more:** [SARA_PERSONA.md](./SARA_PERSONA.md)

---

## 🎯 Features

✅ **Intelligent Scam Detection** - Multi-pattern analysis with confidence scoring
✅ **Sara - AI Agent** - Natural Indian persona that sounds completely real
✅ **Hinglish Conversations** - Natural Hindi-English mix like real Indians speak
✅ **Intelligence Extraction** - Automatically extracts bank accounts, UPI IDs, phone numbers, links
✅ **Multi-turn Conversations** - Maintains context across conversation history
✅ **Human-like Behavior** - Confused, hesitant, with environmental context (school, network issues)
✅ **Automatic Reporting** - Sends final intelligence to GUVI evaluation endpoint
✅ **REST API** - Easy integration with FastAPI
✅ **Secure Authentication** - API key protection

## 🏗️ Architecture

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
```

## 🔑 API Key

**Your API Key:** `HONEY-POT-SECURE-KEY-2024-GUVI-HACK`

Include this in the `x-api-key` header for all requests.

## 📦 Installation

### Method 1: Local Setup

```bash
# Clone/navigate to project directory
cd scam-honeypot-agent

# Install dependencies
pip install -r requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY="your-api-key-here"

# Run the server
python main.py
```

### Method 2: Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up -d

# Check logs
docker-compose logs -f
```

### Method 3: Manual Docker

```bash
# Build image
docker build -t scam-honeypot-agent .

# Run container
docker run -d \
  -p 8000:8000 \
  -e ANTHROPIC_API_KEY="your-api-key-here" \
  --name honeypot \
  scam-honeypot-agent
```

## 🚀 API Endpoints

### 1. Health Check
```bash
GET /health
```

### 2. Root Information
```bash
GET /
```

### 3. Detect & Respond (Main Endpoint)
```bash
POST /api/detect
Headers:
  x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
  Content-Type: application/json

Body:
{
  "sessionId": "unique-session-id",
  "message": {
    "sender": "scammer",
    "text": "Your bank account will be blocked today. Verify immediately.",
    "timestamp": 1770005528731
  },
  "conversationHistory": [],
  "metadata": {
    "channel": "SMS",
    "language": "English",
    "locale": "IN"
  }
}

Response:
{
  "status": "success",
  "reply": "Why will my account be blocked?"
}
```

### 4. Get Session Information
```bash
GET /api/session/{session_id}
Headers:
  x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
```

### 5. Manual Session End
```bash
POST /api/manual-end/{session_id}
Headers:
  x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK
```

## 🧪 Testing

Run the test suite:

```bash
python test_api.py
```

This will:
1. Check health endpoint
2. Simulate a scam conversation
3. Test legitimate messages
4. Trigger manual session end
5. Display extracted intelligence

## 📝 Example Usage

### cURL Example

```bash
curl -X POST http://localhost:8000/api/detect \
  -H "x-api-key: HONEY-POT-SECURE-KEY-2024-GUVI-HACK" \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

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

## 🎭 How It Works

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
```

## 🔒 Security Features

- API Key authentication on all endpoints
- No personal data storage (session-based only)
- Rate limiting ready
- Secure environment variable handling
- Docker containerization

## 📊 Evaluation Criteria Coverage

✅ **Scam Detection Accuracy**: Multi-pattern analysis with confidence scoring
✅ **Quality of Agentic Engagement**: Claude AI generates contextual responses
✅ **Intelligence Extraction**: Regex-based extraction of all required data types
✅ **API Stability**: FastAPI with error handling and logging
✅ **Ethical Behavior**: No impersonation, no illegal instructions, responsible engagement

## 🌐 Deployment

### Deploy to Cloud (Railway/Render/Heroku)

1. Push code to GitHub
2. Connect to your cloud platform
3. Set environment variable: `ANTHROPIC_API_KEY`
4. Deploy!

### Ngrok for Local Testing

```bash
# Run server locally
python main.py

# In another terminal
ngrok http 8000
```

Use the ngrok URL as your public endpoint.

## 📋 Environment Variables

```bash
ANTHROPIC_API_KEY=your-anthropic-api-key
API_KEY=HONEY-POT-SECURE-KEY-2024-GUVI-HACK
PORT=8000
HOST=0.0.0.0
```

## 🤝 Scam Categories Detected

1. **Bank Fraud** - Account blocking threats
2. **UPI Fraud** - Payment redirection scams
3. **Phishing** - Fake links and credentials theft
4. **OTP Scams** - One-time password requests
5. **Prize/Lottery** - Fake rewards
6. **Authority Impersonation** - Fake government/bank officials
7. **Urgency Tactics** - Time pressure scams

## 📞 Support

For issues or questions:
- Check logs: `docker-compose logs -f`
- Test with: `python test_api.py`
- Verify health: `curl http://localhost:8000/health`

## 📄 License

Created for GUVI Hackathon 2024

---

**API Key:** `HONEY-POT-SECURE-KEY-2024-GUVI-HACK`

**Endpoint:** `http://your-server:8000/api/detect`

**Status:** ✅ Production Ready
